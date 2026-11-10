import json
import logging
from datetime import datetime, timezone

import pytest
from telegram import Chat, InaccessibleMessage, Message
from telegram.error import BadRequest, InvalidToken
from telegram.ext import CallbackQueryHandler, CommandHandler

import logger as bot_logger
import telegram_bot

FAKE_TOKEN = "1234567890:AAFakeTokenForTestsOnlyAbCdEfGhIjKlMn"
EXPECTED_LINES = 3
CHAT = Chat(id=42, type="private")


@pytest.fixture(params=telegram_bot.available_languages())
def language(request):
    return request.param


@pytest.fixture
def clean_logging():
    """Snapshot and restore global logging state touched by get_logger and install_secret_redaction."""
    root = logging.getLogger()
    bot = logging.getLogger(bot_logger.DEFAULT_LOG_ROOT)
    saved = {
        "root_handlers": list(root.handlers),
        "root_level": root.level,
        "bot_handlers": list(bot.handlers),
        "bot_level": bot.level,
        "bot_propagate": bot.propagate,
        "factory": logging.getLogRecordFactory(),
    }
    yield
    for handler in root.handlers:
        if handler not in saved["root_handlers"]:
            root.removeHandler(handler)
    for handler in bot.handlers:
        if handler not in saved["bot_handlers"]:
            handler.close()
            bot.removeHandler(handler)
    root.setLevel(saved["root_level"])
    bot.setLevel(saved["bot_level"])
    bot.propagate = saved["bot_propagate"]
    logging.setLogRecordFactory(saved["factory"])


##### Language files


def test_every_language_builds_an_application(language):
    states = telegram_bot.load_states(language)
    app = telegram_bot.build_application(FAKE_TOKEN, states)
    handlers = app.handlers[0]
    assert sum(isinstance(h, CommandHandler) for h in handlers) == 1, "exactly one /start handler"
    assert sum(isinstance(h, CallbackQueryHandler) for h in handlers) == len(states)
    assert telegram_bot.on_error in app.error_handlers


def test_every_keyboard_button_points_at_an_existing_state(language):
    states = telegram_bot.load_states(language)
    patterns = {state["pattern"] for state in states.values()}
    for name, state in states.items():
        for row in state.get("keyboard", []):
            for button in row:
                assert button["next_item"] in patterns, f"{language}/{name}: dangling next_item {button['next_item']!r}"


def test_patterns_are_unique_within_a_language(language):
    """The first matching handler wins, so a duplicate pattern would silently shadow a state."""
    patterns = [state["pattern"] for state in telegram_bot.load_states(language).values()]
    assert len(patterns) == len(set(patterns)), f"{language}: duplicate patterns"


##### Handlers


def test_callback_patterns_match_exactly():
    handler = telegram_bot.make_callback_handler("text", "s1")
    assert handler.pattern.match("s1")
    assert handler.pattern.match("s1-evil") is None
    assert handler.pattern.match("xs1") is None
    assert handler.pattern.match("s1\n") is None, "$ would accept a trailing newline"
    # regex metacharacters in a pattern are treated literally
    handler = telegram_bot.make_callback_handler("text", "a.b")
    assert handler.pattern.match("a.b")
    assert handler.pattern.match("axb") is None


class _FakeMessage:
    def __init__(self):
        self.replies = []

    async def reply_text(self, text, reply_markup):
        self.replies.append((text, reply_markup))


class _FakeBot:
    def __init__(self):
        self.sent = []

    async def send_message(self, chat_id, text, reply_markup):
        self.sent.append((chat_id, text, reply_markup))


class _FakeContext:
    def __init__(self, error=None):
        self.bot = _FakeBot()
        self.error = error


class _FakeQuery:
    def __init__(self, message, edit_error=None):
        self.message = message
        self.answered = False
        self.edited = []
        self.edit_error = edit_error

    async def answer(self):
        self.answered = True

    async def edit_message_text(self, text, reply_markup):
        if self.edit_error:
            raise self.edit_error
        self.edited.append((text, reply_markup))


class _FakeUpdate:
    def __init__(self, message=None, callback_query=None):
        self.message = message
        self.callback_query = callback_query


def _real_message():
    return Message(message_id=7, date=datetime.now(timezone.utc), chat=CHAT)


@pytest.mark.asyncio
async def test_start_handler_replies_with_menu():
    handler = telegram_bot.make_start_handler("welcome", "markup")
    message = _FakeMessage()
    await handler.callback(_FakeUpdate(message=message), _FakeContext())
    assert message.replies == [("welcome", "markup")]
    # An update without a message (e.g. an edited channel post) is ignored rather than crashing.
    await handler.callback(_FakeUpdate(message=None), _FakeContext())


@pytest.mark.asyncio
async def test_callback_handler_answers_and_edits():
    handler = telegram_bot.make_callback_handler("hello", "s1")
    context = _FakeContext()

    query = _FakeQuery(_real_message())
    await handler.callback(_FakeUpdate(callback_query=query), context)
    assert query.answered and query.edited == [("hello", None)]
    assert context.bot.sent == []

    # Re-pressing the current menu's button: Telegram answers "message is not modified"; swallow it.
    query = _FakeQuery(_real_message(), edit_error=BadRequest("Message is not modified: nothing to edit"))
    await handler.callback(_FakeUpdate(callback_query=query), context)
    assert query.answered and context.bot.sent == []

    # Any other API error still surfaces.
    query = _FakeQuery(_real_message(), edit_error=BadRequest("Chat not found"))
    with pytest.raises(BadRequest):
        await handler.callback(_FakeUpdate(callback_query=query), context)


@pytest.mark.asyncio
async def test_callback_handler_sends_new_message_when_edit_impossible():
    handler = telegram_bot.make_callback_handler("hello", "s1", reply_markup="markup")

    # Message older than 48 hours: Telegram refuses the edit, so the menu is sent as a new message.
    context = _FakeContext()
    query = _FakeQuery(_real_message(), edit_error=BadRequest("Message can't be edited"))
    await handler.callback(_FakeUpdate(callback_query=query), context)
    assert query.answered and context.bot.sent == [(CHAT.id, "hello", "markup")]

    # Inaccessible message (Bot API 7+): no edit attempted, menu sent afresh to the same chat.
    context = _FakeContext()
    query = _FakeQuery(InaccessibleMessage(chat=CHAT, message_id=7))
    await handler.callback(_FakeUpdate(callback_query=query), context)
    assert query.answered and query.edited == [] and context.bot.sent == [(CHAT.id, "hello", "markup")]

    # No message at all: nothing to do beyond answering.
    context = _FakeContext()
    query = _FakeQuery(None)
    await handler.callback(_FakeUpdate(callback_query=query), context)
    assert query.answered and context.bot.sent == []


@pytest.mark.asyncio
async def test_error_handler_logs_one_line(caplog):
    with caplog.at_level(logging.ERROR, logger="tblogger.telegram_bot"):
        await telegram_bot.on_error(None, _FakeContext(error=TypeError("Cannot edit an inaccessible message")))
    assert len(caplog.records) == 1
    assert "TypeError: Cannot edit an inaccessible message" in caplog.records[0].getMessage()


##### Configuration


def test_resolve_language_prefers_cli_and_rejects_unknown(monkeypatch):
    monkeypatch.setenv("TELEGRAM_BOT_LANGUAGE", "fa")
    assert telegram_bot.resolve_language("en") == "en"
    assert telegram_bot.resolve_language(None) == "fa"
    with pytest.raises(SystemExit):
        telegram_bot.resolve_language("../../etc")
    monkeypatch.delenv("TELEGRAM_BOT_LANGUAGE")
    with pytest.raises(SystemExit):
        telegram_bot.resolve_language(None)


def test_log_dir_defaults_next_to_code(monkeypatch, tmp_path):
    monkeypatch.delenv("TELEGRAM_BOT_LOG_DIR", raising=False)
    assert telegram_bot.log_dir() == telegram_bot.BASE_DIR
    monkeypatch.setenv("TELEGRAM_BOT_LOG_DIR", str(tmp_path))
    assert telegram_bot.log_dir() == tmp_path


def test_resolve_token_order(tmp_path, monkeypatch):
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN_PATH", raising=False)
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)

    cli_file = tmp_path / "cli.json"
    cli_file.write_text(json.dumps({"en": "cli-token"}))
    env_file = tmp_path / "env.json"
    env_file.write_text(json.dumps({"en": "env-file-token"}))

    monkeypatch.setenv("TELEGRAM_BOT_TOKEN_PATH", str(env_file))
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "env-var-token")

    assert telegram_bot.resolve_token(str(cli_file), "en") == "cli-token"
    assert telegram_bot.resolve_token(str(tmp_path / "missing.json"), "en") == "env-file-token"
    assert telegram_bot.resolve_token(None, "en") == "env-file-token"
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN_PATH", str(tmp_path / "missing.json"))
    assert telegram_bot.resolve_token(None, "en") == "env-var-token"
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN")
    with pytest.raises(SystemExit):
        telegram_bot.resolve_token(None, "en")


@pytest.mark.parametrize(
    "content",
    [
        '{"en": "secret-looking-value"',  # truncated JSON
        '{"fa": "secret-looking-value"}',  # other language only
        '["secret-looking-value"]',  # not an object
        '"secret-looking-value"',  # bare string
        '{"en": ""}',  # empty token
        '{"en": 12345}',  # wrong type
    ],
)
def test_token_file_errors_do_not_echo_contents(tmp_path, content):
    path = tmp_path / "tok.json"
    path.write_text(content)
    with pytest.raises(SystemExit) as exc:
        telegram_bot.read_token_file(str(path), "en")
    assert "secret-looking-value" not in str(exc.value)
    assert "12345" not in str(exc.value)


def test_parse_log_level_accepts_names_and_numbers():
    assert bot_logger.parse_log_level(None) == logging.INFO
    assert bot_logger.parse_log_level("") == logging.INFO
    assert bot_logger.parse_log_level("DEBUG") == logging.DEBUG
    assert bot_logger.parse_log_level("warning") == logging.WARNING
    assert bot_logger.parse_log_level("10") == logging.DEBUG
    assert bot_logger.parse_log_level("0") == 0
    with pytest.raises(SystemExit):
        bot_logger.parse_log_level("LOUD")


##### Redaction


def _collector(logger_name):
    records = []

    class Collector(logging.Handler):
        def emit(self, record):
            records.append(self.format(record))

    handler = Collector()
    handler.setFormatter(logging.Formatter("%(message)s"))
    lg = logging.getLogger(logger_name)
    lg.addHandler(handler)
    lg.setLevel(logging.DEBUG)
    return lg, handler, records


def test_redaction_scrubs_message_args_and_tracebacks(clean_logging):
    lg, handler, records = _collector("test.redaction")
    redactor = bot_logger.install_secret_redaction(FAKE_TOKEN)
    try:
        url = f"https://api.telegram.org/bot{FAKE_TOKEN}/getUpdates"
        lg.error("Error while getting updates: %s", RuntimeError(f"Max retries exceeded with url: {url}"))
        try:
            raise ValueError(url)
        except ValueError:
            lg.exception("boom")
        lg.info("plain message without secrets")
    finally:
        redactor.uninstall()
        lg.removeHandler(handler)

    assert len(records) == EXPECTED_LINES
    for line in records:
        assert FAKE_TOKEN not in line
    assert bot_logger.REDACTED in records[0]
    assert "Traceback" in records[1] and bot_logger.REDACTED in records[1]
    assert records[2] == "plain message without secrets"

    # After uninstall, logging is back to normal.
    lg.addHandler(handler)
    try:
        lg.info("token=%s", FAKE_TOKEN)
    finally:
        lg.removeHandler(handler)
    assert FAKE_TOKEN in records[-1]


def test_redaction_covers_handlers_added_later(clean_logging):
    """Installing the redactor before any handler exists must still protect handlers created afterwards."""
    redactor = bot_logger.install_secret_redaction(FAKE_TOKEN)
    lg, handler, records = _collector("test.redaction.later")
    try:
        lg.error("leak %s", FAKE_TOKEN)
    finally:
        redactor.uninstall()
        lg.removeHandler(handler)
    assert records == [f"leak {bot_logger.REDACTED}"]


def test_real_logger_wiring_scrubs_library_errors(clean_logging, tmp_path, capsys):
    """get_logger + install_secret_redaction: library errors reach the console scrubbed, bot errors reach both."""
    log_file = tmp_path / "bot.log"
    bot_logger.get_logger("telegram_bot:en", log_path=log_file)
    redactor = bot_logger.install_secret_redaction(FAKE_TOKEN)
    try:
        logging.getLogger("telegram.ext").error("library says token `%s` was rejected", FAKE_TOKEN)
        logging.getLogger("tblogger.telegram_bot").error("bot says %s", FAKE_TOKEN)
        logging.getLogger("httpx").info("HTTP Request: POST https://api.telegram.org/bot%s/getMe", FAKE_TOKEN)
    finally:
        redactor.uninstall()

    console = capsys.readouterr().err
    assert FAKE_TOKEN not in console
    assert "library says token `<redacted>` was rejected" in console
    assert console.count("bot says <redacted>") == 1, "bot records must not be duplicated on the console"
    assert "HTTP Request" not in console, "httpx request logging must be suppressed"

    file_lines = [json.loads(line) for line in log_file.read_text().splitlines()]
    assert FAKE_TOKEN not in log_file.read_text()
    assert [entry["message"] for entry in file_lines] == ["bot says <redacted>"]


##### Entrypoint


class _FailingApplication:
    def __init__(self, error):
        self.error = error

    def run_polling(self, **kwargs):
        raise self.error


def test_main_exits_cleanly_on_invalid_token(clean_logging, monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("TELEGRAM_BOT_LOG_DIR", str(tmp_path))
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", FAKE_TOKEN)
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN_PATH", raising=False)
    error = InvalidToken(f"The token `{FAKE_TOKEN}` was rejected by the server.")
    monkeypatch.setattr(
        telegram_bot, "build_application", lambda token, states, post_init=None: _FailingApplication(error)
    )

    with pytest.raises(SystemExit) as exc:
        telegram_bot.main(["--language", "en"])
    assert exc.value.code == 1

    console = capsys.readouterr().err
    assert FAKE_TOKEN not in console
    assert "Telegram rejected the bot token for language en" in console
    log_text = (tmp_path / "telegram_bot_en.log").read_text()
    assert FAKE_TOKEN not in log_text
    assert "Telegram rejected the bot token" in log_text


def test_main_scrubs_unexpected_errors(clean_logging, monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("TELEGRAM_BOT_LOG_DIR", str(tmp_path))
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", FAKE_TOKEN)
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN_PATH", raising=False)
    error = RuntimeError(f"connect failed for https://api.telegram.org/bot{FAKE_TOKEN}/getUpdates")
    monkeypatch.setattr(
        telegram_bot, "build_application", lambda token, states, post_init=None: _FailingApplication(error)
    )

    with pytest.raises(SystemExit) as exc:
        telegram_bot.main(["--language", "en"])
    assert exc.value.code == 1
    console = capsys.readouterr().err
    assert FAKE_TOKEN not in console
    assert "Traceback" in console and bot_logger.REDACTED in console
