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

from typing import Optional
import tempfile, logging, logging.handlers, os, json

DEFAULT_LOG_ROOT: str = "tblogger"
DEFAULT_TEXT_FORMATTER = logging.Formatter("[%(asctime)s] (%(name)s)  %(levelname)s: %(message)s")
DEFAULT_LOG_LEVEL: int = int(os.getenv("TELEGRAM_BOT_LOG_LEVEL", str(logging.DEBUG)))

def get_logger(
    name: str,
    log_path: Optional[str] = None,
    log_root: str = DEFAULT_LOG_ROOT,
    log_level: Optional[int] = None,

) -> logging.Logger:

  if log_path is None:
 	  log_path = tempfile.NamedTemporaryFile(prefix="telegram_bot_", suffix=".log")
  if not log_path.is_file():
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.touch(exist_ok=True)

  if (not log_level):
    log_level = DEFAULT_LOG_LEVEL

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

  logger.addHandler(console_handler)
  logger.addHandler(file_handler)
  logger.setLevel(log_level)
  return logger

class JSONFormatter(logging.Formatter):
    """A class to generate log lines from the given format"""

    def format(self, record):
        """
        Formats the record's field attributes and returns a formatted log line
        :param record: this is a JSON formatted string containing the field attributes
        :return: This method returns a JSON formatted string using the class's specified format
        """

        j = {}
        for field in json.loads(self._fmt).keys():
            j.update({field: getattr(record, field)})
        # incorporate exception stack into json log line if it is present
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

DEFAULT_JSON_FORMATTER = JSONFormatter(
    json.dumps({field: "%(" + field + ")s" for field in JSON_FIELDS})
)

