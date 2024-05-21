states = {
    "activity": {
        "message": "🤖Добро пожаловать на телеграм-канал Psiphon 👋",
        "pattern": "activity",
        "keyboard": [
            [{"text": "Скачать приложение Psiphon 👻", "next_item": "m2"}],
            [{"text": "Часто задаваемые вопросы (FAQ) 🧐", "next_item": "m3"}],
            [{"text": "Подпишитесь на нас 🐦", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "🤖Пожалуйста, выберите свою операционную систему 🖥️",
        "pattern": "m2",
        "keyboard": [
            [{"text": "Windows", "next_item": "s1"}],
            [{"text": "Android", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "Возврат ⬅️ ", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "🤖       Пожалуйста, выберите вопрос",
        "pattern": "m3",
        "keyboard": [
            [{"text": "Что делать, если Psiphon не подключается?", "next_item": "f1"}],
            [{"text": "Как обновить Psiphon?", "next_item": "f3"}],
            [{"text": "У меня другой вопрос.", "next_item": "f2"}],
            [{"text": "Возврат ⬅️ ", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "Будь на связи",
        "pattern": "m4",
        "keyboard": [
            [{"text": "Facebook", "next_item": "sm1"}],
            [{"text": "Твиттер", "next_item": "sm2"}],
            [{"text": "Сайт", "next_item": "sm3"}],
            [{"text": "Возврат ⬅️", "next_item": "activity"}],
        ],
    },
    "windows download": {
        "message": "https://s3.amazonaws.com/psiphon/web/mmqu-p8qj-sgdq/psiphon3.exe",
        "pattern": "s1",
    },
    "android download": {
        "message": "https://s3.amazonaws.com/psiphon/web/mmqu-p8qj-sgdq/PsiphonAndroid.apk",
        "pattern": "s3",
    },
    "ios download": {
        "message": "https://itunes.apple.com/app/psiphon/id1276263909?ls=1&mt=8",
        "pattern": "s4",
    },
    "faq q1": {
        "message": ""
        "1) Убедитесь, что приложение Psiphon обновлено до последней версии\n"
        "2) Подождите несколько минут, пока Psiphon выберет лучший способ подключения\n"
        "3) Отправте отзыв через приложение Psiphon\n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/ru/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "Android: Если вы установили Psiphon из Google Play Store, то обновление произойдет автоматически, как только новая версия станет доступной. Если Psiphon был установлен другим способом, то Psiphon скачает новую версию и попросит установить обновление.\n\n"
        "Windows: Psiphon для Windows автоматически скачает и установит обновление, как только оно останет доступно.\n\n"
        "iOS: App Store будет автоматически обновлять Psiphon с вашего разрешения.",
        "pattern": "f3",
    },
    "share facebook": {
        "message": "https://www.facebook.com/Psiphon-207377692624236/",
        "pattern": "sm1",
    },
    "share twitter": {
        "message": "https://twitter.com/psiphoninc",
        "pattern": "sm2",
    },
    "share website": {
        "message": "https://psiphon.ca",
        "pattern": "sm3",
    },
}
