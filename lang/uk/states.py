states = {
    "activity": {
        "message": "🤖Ласкаво просимо до телеграм-каналу Psiphon👋",
        "pattern": "activity",
        "keyboard": [
            [{"text": "Завантажити додаток Psiphon 👻", "next_item": "m2"}],
            [{"text": "Часті запитання (FAQ) 🧐", "next_item": "m3"}],
            [{"text": "Підпишіться на нас 🐦", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "🤖Будь ласка, оберіть вашу операційну систему 🖥️",
        "pattern": "m2",
        "keyboard": [
            [{"text": "Windows", "next_item": "s1"}],
            [{"text": "Android", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "Повернутись ⬅️ ", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "🤖        Будь ласка, оберіть ваше запитання",
        "pattern": "m3",
        "keyboard": [
            [{"text": "Psiphon не встановлює з'єднання?", "next_item": "f1"}],
            [{"text": "Як оновити Psiphon?", "next_item": "f3"}],
            [{"text": "В мене інше питання.", "next_item": "f2"}],
            [{"text": "Повернутись ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "Будь на зв'язку",
        "pattern": "m4",
        "keyboard": [
            [{"text": "Facebook", "next_item": "sm1"}],
            [{"text": "Твіттер", "next_item": "sm2"}],
            [{"text": "Сайт", "next_item": "sm3"}],
            [{"text": "Повернутись ⬅️", "next_item": "activity"}],
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
        "1) Переконайтеся, що ваш додаток Psiphon оновленно до останньої версії\n"
        "2) Зачекайте кілька хвилин, доки Psiphon знайде найкращий спосіб підключення\n"
        "3) Надішліть ваш відгук через додаток Psiphon\n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/uk/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "Android: Якщо ви завантажили Psiphon з Google Play Store, додаток буде автоматично оновлюватись до останньої версії. Якщо ви завантажили Psiphon іншим способом, додаток автоматично завантажить оновлення та надішле запит на його встановлення.\n\n"
        "Windows: Psiphon для Windows буде автоматично оновлюватись до останньої версії.\n\n"
        "iOS: App Store буде автоматично оновлювати додаток з вашого дозволу.",
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
    "share instagram": {
        "message": "https://psiphon.ca",
        "pattern": "sm3",
    },
}
