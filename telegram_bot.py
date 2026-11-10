#!/usr/bin/env python3

#    Psiphon Telegram Bots
#    Copyright (C) 2021 Psiphon Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import importlib
import json
import logging
import os
import re
from pathlib import Path
from typing import Callable, Coroutine, Optional

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update
from telegram.error import BadRequest, InvalidToken
from telegram.ext import Application, ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

from logger import get_logger, install_secret_redaction

BASE_DIR = Path(__file__).resolve().parent
LANG_DIR = BASE_DIR / "lang"

log = logging.getLogger("tblogger.telegram_bot")


##### Configuration


def available_languages() -> list:
    """Language codes that have a lang/<code>/states.py file."""
    return sorted(p.name for p in LANG_DIR.iterdir() if p.is_dir() and (p / "states.py").is_file())


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--language", help="language code as in ./lang/. Default: $TELEGRAM_BOT_LANGUAGE")
    parser.add_argument(
        "-t",
        "--token",
        help="path to JSON file containing Telegram bot HTTP API token",
        metavar="PATH",
    )
    return parser.parse_args(argv)


def resolve_language(cli_language: Optional[str]) -> str:
    """Pick the language from the CLI or environment and check it against the lang/ directory.

    The value is used to build an import path and a log file name, so it must be one of the
    known codes rather than an arbitrary string.
    """
    language = cli_language or os.getenv("TELEGRAM_BOT_LANGUAGE")
    if not language:
        raise SystemExit("no language found: pass --language or set TELEGRAM_BOT_LANGUAGE")
    known = available_languages()
    if language not in known:
        raise SystemExit(f"unknown language {language!r}; available: {', '.join(known)}")
    return language


def log_dir() -> Path:
    """Directory for the JSON log file: $TELEGRAM_BOT_LOG_DIR, or next to the code."""
    configured = os.getenv("TELEGRAM_BOT_LOG_DIR")
    return Path(configured) if configured else BASE_DIR


def read_token_file(path: str, language: str) -> Optional[str]:
    """Return the token for `language` from the JSON file at `path`, or None if the file is missing."""
    try:
        data = json.loads(Path(path).read_text())
    except FileNotFoundError:
        log.info("No token file found at %s", path)
        return None
    except json.JSONDecodeError as e:
        # Deliberately do not include file contents in the error.
        raise SystemExit(f"token file {path} is not valid JSON: line {e.lineno} column {e.colno}") from None
    if not isinstance(data, dict) or language not in data:
        raise SystemExit(f"token file {path} has no entry for language {language!r}")
    token = data[language]
    if not isinstance(token, str) or not token:
        raise SystemExit(f"token for language {language!r} in {path} must be a non-empty string")
    return token


def resolve_token(cli_token_path: Optional[str], language: str) -> str:
    """Token lookup order: --token file, then $TELEGRAM_BOT_TOKEN_PATH file, then $TELEGRAM_BOT_TOKEN."""
    for path in (cli_token_path, os.getenv("TELEGRAM_BOT_TOKEN_PATH")):
        if path:
            token = read_token_file(path, language)
            if token:
                return token
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("No token or token file found")
    return token


def load_states(language: str) -> dict:
    module = importlib.import_module(f"lang.{language}.states")
    return module.states


##### Keyboards


def build_keyboard(buttons) -> InlineKeyboardMarkup:
    keyboard = []
    for row in buttons:
        keyboard.append([InlineKeyboardButton(button["text"], callback_data=button["next_item"]) for button in row])
    return InlineKeyboardMarkup(keyboard)


##### Handlers


def make_start_handler(text: str, reply_markup: Optional[InlineKeyboardMarkup]) -> CommandHandler:
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        log.info("new interaction started")
        if update.message is None:
            return
        await update.message.reply_text(text, reply_markup=reply_markup)

    return CommandHandler("start", handler)


def _cannot_edit(error: BadRequest) -> bool:
    reason = str(error).lower()
    return "can't be edited" in reason or "cannot be edited" in reason


def make_callback_handler(
    text: str, pattern: str, reply_markup: Optional[InlineKeyboardMarkup] = None
) -> CallbackQueryHandler:
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.callback_query
        # Always acknowledge, otherwise the client shows a spinner until it times out.
        await query.answer()
        message = query.message
        if isinstance(message, Message):
            try:
                await query.edit_message_text(text=text, reply_markup=reply_markup)
                return
            except BadRequest as e:
                # Pressing the button for the menu that is already shown is not an error worth logging.
                if "not modified" in str(e).lower():
                    return
                if not _cannot_edit(e):
                    raise
        if message is None:
            return
        # The original message is too old to edit (48 hours) or no longer accessible: send the menu afresh.
        # InaccessibleMessage still carries the chat it belongs to.
        await context.bot.send_message(chat_id=message.chat.id, text=text, reply_markup=reply_markup)

    # Anchor the pattern so callback data is matched exactly, not by prefix. \A and \Z, unlike ^ and $,
    # do not let a trailing newline through.
    return CallbackQueryHandler(handler, pattern=re.compile(rf"\A{re.escape(pattern)}\Z"))


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log one concise line per failed update instead of the library's full traceback."""
    error = context.error
    log.error("Error while handling an update: %s: %s", type(error).__name__, error)


PostInit = Callable[[Application], Coroutine[None, None, None]]


def build_application(token: str, states: dict, post_init: Optional[PostInit] = None) -> Application:
    builder = ApplicationBuilder().token(token)
    if post_init is not None:
        builder = builder.post_init(post_init)
    application = builder.build()
    for state in states.values():
        keyboard = build_keyboard(state["keyboard"]) if "keyboard" in state else None
        if state["pattern"] == "activity":
            application.add_handler(make_start_handler(state["message"], keyboard))
        application.add_handler(make_callback_handler(state["message"], state["pattern"], keyboard))
    application.add_error_handler(on_error)
    return application


##### Bot Entrypoint


def main(argv=None) -> None:
    args = parse_args(argv)
    language = resolve_language(args.language)

    get_logger(
        f"telegram_bot:{language}",
        log_path=log_dir() / f"telegram_bot_{language}.log",
    )

    token = resolve_token(args.token, language)
    # The token appears in request URLs; make sure no log line can carry it.
    install_secret_redaction(token)

    states = load_states(language)

    async def on_ready(application: Application) -> None:
        # Runs after the token has been verified with Telegram.
        log.info("telegram bot (%s) is listening as @%s", language, application.bot.username)

    application = build_application(token, states, post_init=on_ready)

    try:
        # bootstrap_retries=-1: keep retrying transient network errors at startup; an invalid token still aborts.
        application.run_polling(allowed_updates=[Update.MESSAGE, Update.CALLBACK_QUERY], bootstrap_retries=-1)
    except InvalidToken:
        # The library's own message quotes the token; replace it with one that does not.
        log.error("Telegram rejected the bot token for language %s", language)
        raise SystemExit(1) from None
    except Exception:
        # Route every fatal error through logging so the redaction filter scrubs it before it is printed.
        log.exception("telegram bot (%s) exited with an unhandled error", language)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
