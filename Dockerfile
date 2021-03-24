FROM python:3.8-alpine

# Set these variables in environment at runtime:
#   TELEGRAM_BOT_LANGUAGE
#   TELEGRAM_BOT_TOKEN_PATH

COPY telegram_bot.py /usr/local/telegram-bot/telegram_bot.py
COPY logger.py /usr/local/telegram-bot/logger.py
COPY lang /usr/local/telegram-bot/lang
COPY requirements.txt /usr/local/telegram-bot/requirements.txt

# Packages needed for Alpine only. Alpine offers 60% reduction in image size. (1GB -> 333MB)
RUN apk update && apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo make
RUN cd /usr/local/telegram-bot && touch config_file.py && pip install -r requirements.txt

# Create new user and change owner of the telegram-bot files
RUN addgroup -S telegram_bot && adduser -S telegram_bot -G telegram_bot && \
    chown -R telegram_bot:telegram_bot /usr/local/telegram-bot
USER telegram_bot
WORKDIR /usr/local/telegram-bot
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
