#!/bin/sh
if [ -z "${TELEGRAM_BOT_LANGUAGE}" ]
then
  echo "Variable TELEGRAM_BOT_LANGUAGE not set."
  echo
  exit 1
fi
if [ -z "${TELEGRAM_BOT_TOKEN_PATH}" ] && [ -z "${TELEGRAM_BOT_TOKEN}" ]
then
  echo "One of TELEGRAM_BOT_TOKEN_PATH or TELEGRAM_BOT_TOKEN must be set."
  echo
  exit 1
fi
if [ ! -z "${TELEGRAM_BOT_TOKEN_PATH}" ]
then
  if [ ! -f ${TELEGRAM_BOT_TOKEN_PATH} ]
  then
    echo "Telegram bot API token file not found: ${TELEGRAM_BOT_TOKEN_PATH}"
    echo
    exit 1
  fi
  if [ ! -s ${TELEGRAM_BOT_TOKEN_PATH} ]
  then
    echo "Please place Telegram bot API token into ${TELEGRAM_BOT_TOKEN_PATH}"
    echo "Example content of api_token.json:"
    echo "{"
    echo "  \"en\": \"0000000000:abcdefghijklmnopqrstuvwxyzAZY1234y8\""
    echo "}"
    echo ""
    exit 1
  fi
fi
python3 /usr/local/telegram-bot/telegram_bot.py
