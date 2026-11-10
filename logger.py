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

import json
import logging
import logging.handlers
import os
import tempfile
from pathlib import Path
from typing import Optional, Union

DEFAULT_LOG_ROOT: str = "tblogger"
DEFAULT_TEXT_FORMATTER = logging.Formatter("[%(asctime)s] (%(name)s)  %(levelname)s: %(message)s")
LOG_LEVEL_ENV = "TELEGRAM_BOT_LOG_LEVEL"

# Third-party loggers that would otherwise log every request URL (which carries the bot token).
NOISY_LIBRARY_LOGGERS = ("httpx", "httpcore", "telegram")

REDACTED = "<redacted>"


def parse_log_level(value: Optional[str], default: int = logging.INFO) -> int:
    """Accept a level name ("DEBUG") or number ("10"); unset or empty means `default`."""
    if value is None or value.strip() == "":
        return default
    text = value.strip()
    if text.isdigit():
        return int(text)
    level = logging.getLevelNamesMapping().get(text.upper())
    if level is None:
        raise SystemExit(f"{LOG_LEVEL_ENV}={value!r} is not a log level name or number")
    return level


class SecretRedactor:
    """Scrubs known secrets out of every log record at creation time.

    Installed as the global LogRecord factory, so it covers every handler on every logger, including
    handlers added after installation and Python's handler of last resort. The message is rendered
    from its args immediately (so a secret hidden in an exception object is caught) and the traceback,
    if any, is rendered and scrubbed as well.
    """

    def __init__(self, secrets):
        self.secrets = [s for s in secrets if s]
        self._previous_factory = None

    def scrub(self, text: str) -> str:
        for secret in self.secrets:
            text = text.replace(secret, REDACTED)
        return text

    def redact(self, record: logging.LogRecord) -> None:
        if not self.secrets:
            return
        try:
            message = record.getMessage()
        except Exception:  # noqa: BLE001 - a bad format string must not break logging
            message = str(record.msg)
        record.msg = self.scrub(message)
        record.args = ()
        if record.exc_info and not record.exc_text:
            record.exc_text = logging.Formatter().formatException(record.exc_info)
        if record.exc_text:
            record.exc_text = self.scrub(record.exc_text)

    def install(self) -> "SecretRedactor":
        previous = logging.getLogRecordFactory()
        self._previous_factory = previous

        def factory(*args, **kwargs):
            record = previous(*args, **kwargs)
            self.redact(record)
            return record

        logging.setLogRecordFactory(factory)
        return self

    def uninstall(self) -> None:
        if self._previous_factory is not None:
            logging.setLogRecordFactory(self._previous_factory)
            self._previous_factory = None


def install_secret_redaction(*secrets: str) -> SecretRedactor:
    """Scrub `secrets` from all log output from now on. Returns the redactor so it can be uninstalled."""
    return SecretRedactor(secrets).install()


def get_logger(
    name: str,
    log_path: Optional[Union[str, Path]] = None,
    log_root: str = DEFAULT_LOG_ROOT,
    log_level: Optional[int] = None,
) -> logging.Logger:
    if log_path is None:
        log_path = Path(tempfile.gettempdir()) / "telegram_bot.log"
    log_path = Path(log_path)
    if not log_path.is_file():
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.touch(exist_ok=True)

    if log_level is None:
        log_level = parse_log_level(os.getenv(LOG_LEVEL_ENV))

    name_components = name.split(".")
    try:
        name_components.remove(log_root)
    except ValueError:
        pass
    name_components.insert(0, log_root)

    logger = logging.getLogger(".".join(name_components))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(DEFAULT_TEXT_FORMATTER)

    file_handler = logging.handlers.WatchedFileHandler(log_path)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(DEFAULT_JSON_FORMATTER)

    # The bot's own messages go to the console and the JSON file.
    bot_logger = logging.getLogger(log_root)
    bot_logger.addHandler(console_handler)
    bot_logger.addHandler(file_handler)
    bot_logger.setLevel(log_level)
    bot_logger.propagate = False

    # Library warnings and errors go to the console only, so a failing network call is visible.
    root = logging.getLogger()
    root.addHandler(console_handler)
    root.setLevel(logging.WARNING)
    for library in NOISY_LIBRARY_LOGGERS:
        logging.getLogger(library).setLevel(logging.WARNING)

    return logger


class JSONFormatter(logging.Formatter):
    """A class to generate log lines from the given format"""

    def format(self, record):
        """
        Formats the record's field attributes and returns a formatted log line
        :param record: this is a JSON formatted string containing the field attributes
        :return: This method returns a JSON formatted string using the class's specified format
        """
        record.message = record.getMessage()
        j = {}
        for field in json.loads(self._fmt).keys():
            j.update({field: getattr(record, field)})
        # incorporate exception stack into json log line if it is present
        if record.exc_info and not record.exc_text:
            record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            j.update({"exception": record.exc_text})
        return json.dumps(j)


JSON_FIELDS = [
    "filename",
    "funcName",
    "levelname",
    "lineno",
    "module",
    "msecs",
    "message",
    "name",
]

DEFAULT_JSON_FORMATTER = JSONFormatter(json.dumps({field: "%(" + field + ")s" for field in JSON_FIELDS}))
