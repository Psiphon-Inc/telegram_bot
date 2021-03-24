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

from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters, Updater
from telegram import ReplyMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from pathlib import Path
from logger import get_logger

import importlib, argparse, sys, os, json

parser = argparse.ArgumentParser()
parser.add_argument("-l","--language",help="language code as in ./lang/. Default: en")
parser.add_argument("-t","--token",help="path to JSON file containing Telegram bot HTTP API token", metavar="PATH")
args = parser.parse_args()

if args.language:
  language = args.language
else:
  language = os.getenv('TELEGRAM_BOT_LANGUAGE')
  if not language:
    raise Exception("no language found")

log = get_logger(f"telegram_bot:{language}", log_path=Path(os.path.join(os.path.dirname(__file__),f"telegram_bot_{language}.log")))

def checkTokenEnv(language, logger):
  token_env_path = os.getenv('TELEGRAM_BOT_TOKEN_PATH')
  if token_env_path:
    try:
      token = json.loads(Path(token_env_path).read_text())[language]
      return token
    except FileNotFoundError:
      log.info(f"No file found at {token_env_path}, will check for token")

  token = os.getenv("TELEGRAM_BOT_TOKEN")
  if not token:
    raise Exception(f"No token or token file found")
  return token

if args.token:
  token_path = args.token
  try:
    token = json.loads(Path(token_path).read_text())[language]
  except FileNotFoundError:
    log.info(f"No file found at {token_path}, will check env vars for token")
    token = checkTokenEnv(language, log)
else:
  token = checkTokenEnv(language, log)

# import
s = importlib.import_module(f"lang.{language}.states")
states = s.states

# token is added to bot
updater = Updater(token)
dispatcher = updater.dispatcher


##### Bot Entrypoint
def getStartHandler(text, reply_markup):
  def handler(bot, update):
    log.info("new interaction started")
    update.message.reply_text(text,
                              reply_markup=reply_markup)
  return CommandHandler('start', handler)

def getCallBackQueryHandler(text, pattern, reply_markup=None, log_info=None):
  def handler(bot, update):
    if log_info:
      log.info(log_info)
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                           message_id=query.message.message_id,
                           text=text,
                           reply_markup=reply_markup if reply_markup else None)
  return CallbackQueryHandler(handler, pattern=pattern)

# more action items come here / callback_data option add them here and remove "pass"
# then add the message in the messages

def first_submenu(bot, update):
  pass

##### Keyboards

def getInlineKeyboard(buttons):
  keyboard = []
  for row in buttons:
    current_row = []
    for button in row:
      current_row.append(InlineKeyboardButton(button['text'], callback_data=button['next_item']))
    keyboard.append(current_row)
  return InlineKeyboardMarkup(keyboard)

##### Handlers

for state in states.values():

  keyboard = None
  if 'keyboard' in state:
    keyboard = getInlineKeyboard(state['keyboard'])
  if state['pattern'] == 'activity':
    updater.dispatcher.add_handler(getStartHandler(state['message'],keyboard))
  updater.dispatcher.add_handler(getCallBackQueryHandler(state['message'], state['pattern'], reply_markup=keyboard))

print(updater.bot.username, 'is listening...')
updater.start_polling()
