# telegram_bot
Psiphon Telegram bots in Arabic, Chinese, English, Persian, Ukrainian and Russian.
Language specific files are located under `lang` folder. Each language has a 'states.py' file that has messages and keyboard layouts. There must be 'activity' state present, 'activity' state is called when `/start` command is issued to the bot.

Dummy states.py file:
```
states = {
  'activity': {
    'message': "Are you using a telegram bot?",
    'pattern': 'activity',
    'keyboard': [
      [{'text': "Yes!", 'next_item': 'y' }],
      [{'text': "No", 'next_item':  'n' }],
    ]
    },
  'yes': {
    'message': "Thank you for using the Telegram bot!",
    'pattern': 'y',
    },
  'no': {
    'message': "Please consider using our Telegram bot",
    'pattern': 'n',
    },
}
```
'keyboard' is a two-dimensional list, each element is a dictionary with 'text' and 'next_item' field. Value of 'next_item' is used to identify what to show when the button is pressed by matching 'next_item' value with 'pattern' value of the menu.


To add a new language create a subfolder under `lang`, name it with a language code and place 'states.py' file in there.

Language can be selected by defining TELEGRAM_BOT_LANGUAGE environment variable or by using `--language` command line argument.

## Telegram API Token
API token can be added to the bot in 3 ways. The format of the file is a `JSON` object where the key is the code for the language, and the value is the api key. First if a path to the token file is specified with `--token`, the script will look there. If no file is found, or no argument is used, the script looks for a path set by the TELEGRAM_BOT_TOKEN_PATH environment variable. If no environment variable is set for the path, the script will looks for a TELEGRAM_BOT_TOKEN environment variable for the token.

Example `api_token.json`:
```
{
  "en": "0000000000:abcdefghijklmnopqrstuvwxyzAZY1234y8"
}
```

To obtain Telegram bot API token follow [this article](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
The `api_token.json` file is not committed and is ignored in `.gitignore`.

## Run

##### Virtual Environment
1. Clone repository
2. Create and activate Python virtual environment ([venv](https://docs.python.org/3/library/venv.html))
3. Install requirements with `pip install -r requirements.txt`
4. Run telegram_bot.py

Examples:
```
# Run Telegram bot in English using API token in api_token.json
$ python3 telegram_bot.py --language en --token ./api_token.json

# Run Telegram bot in Arabic using API token in api_token.json
$ python3 telegram_bot.py --language ar --token ./api_token.json

OR

$ TELEGRAM_BOT_LANGUAGE=ar TELEGRAM_BOT_TOKEN_PATH=./api_token.json python3 telegram_bot.py

OR

$ TELEGRAM_BOT_LANGUAGE=ar TELEGRAM_BOT_TOKEN=abcdefghijklmnopqrstuvwxyzAZY1234y8 python3 telegram_bot.py
```

##### Docker
1) Make sure api_token.json contains a valid API token
2) Execute `docker-compose up -d`

To change language modify TELEGRAM_BOT_LANGUAGE inside docker-compose.yaml file.

##### Running Multiple Instances
To run multiple instances create multiple Telegram bots and you have the option to have the  api_tokens in the same JSON file, or have them in separate JSON files.
For example to run AR and EN versions create two bots and save their API tokens to api_token.json. Use same format as before.

Example `api_tokens.json`:
```
{
  "en": "0000000000:abcdefghijklmnopqrstuvwxyzAZY1234y8",
  "ar": "0000000000:njlakflklqkjf3498762835fkjgksjhjhqq"
}
```
Now edit `docker-compose.yaml` file and include entry for each language (with corresponding `volumes` and `environment`). For example:
```
# ./docker-compose.yaml

version: '2'
x-tb: &default-config
...
x-volumes:
  &api_tokens
  - ./api_token.json:/usr/local/telegram-bot/api_tokens.json
services:
    telegram-bot-en:
        <<: *default-config
        environment:
          - TELEGRAM_BOT_LANGUAGE=en
        volumes: *api_tokens

    telegram-bot-ar:
        <<: *default-config
        environment:
          - TELEGRAM_BOT_LANGUAGE=ar
        volumes: *api_tokens
```

OR

run without Docker
```
. ./venv/bin/activate
./telegram_bot.py -t api_token.json -l en &
./telegram_bot.py -t api_token.json -l ar &
```
