# Pinned by digest so the base image cannot change under us. Update the tag and digest together.
ARG PYTHON_IMAGE=python:3.13-alpine@sha256:7984cf56ceaddebe4fefeb75d64000b9f45d8b77b11a09b24524da6cdc3af0c8

# Stage 1: install dependencies. python-telegram-bot and httpx are pure Python, so no compiler is needed.
# requirements.txt is a fully pinned, hashed lockfile (see README), so every package is verified.
FROM ${PYTHON_IMAGE} AS build
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes --prefix=/install -r requirements.txt

# Stage 2: runtime image with only the interpreter, the installed packages and the bot.
FROM ${PYTHON_IMAGE}

# Set these variables in environment at runtime:
#   TELEGRAM_BOT_LANGUAGE
#   TELEGRAM_BOT_TOKEN_PATH (or TELEGRAM_BOT_TOKEN)

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TELEGRAM_BOT_LOG_DIR=/var/log/telegram-bot

# Fixed, numeric UID/GID so Kubernetes `runAsNonRoot` can verify the user without a name lookup.
RUN addgroup -S -g 10001 telegram_bot && adduser -S -u 10001 -G telegram_bot telegram_bot && \
    mkdir -p /var/log/telegram-bot && chown telegram_bot:telegram_bot /var/log/telegram-bot

COPY --from=build /install /usr/local

# Code stays owned by root so the runtime user cannot modify it; only the log directory is writable.
WORKDIR /usr/local/telegram-bot
COPY telegram_bot.py logger.py ./
COPY lang ./lang
COPY entrypoint.sh /entrypoint.sh

USER 10001:10001
ENTRYPOINT ["/entrypoint.sh"]
