states = {
    "activity": {
        "message": "🤖Psiphon Telegram Bot uygulamasına hoş geldiniz",
        "pattern": "activity",
        "keyboard": [
            [{"text": "Psiphon uygulamasını indir", "next_item": "m2"}],
            [{"text": "Sık Sorulan Sorular", "next_item": "m3"}],
            [{"text": "Sosyal ağlar", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "Lütfen işletim sisteminizi seçin",
        "pattern": "m2",
        "keyboard": [
            [{"text": "Windows", "next_item": "s1"}],
            [{"text": "Android", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "Geri ⬅️", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "Lütfen sorunuzu seçin",
        "pattern": "m3",
        "keyboard": [
            [{"text": "Psiphon çalışmıyor", "next_item": "f1"}],
            [{"text": "Psiphon nasıl güncellenir?", "next_item": "f3"}],
            [{"text": "Farklı bir sorum var", "next_item": "f2"}],
            [{"text": "Geri ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "Psiphon uygulamasını izleyin",
        "pattern": "m4",
        "keyboard": [
            [{"text": "Facebook", "next_item": "sm1"}],
            [{"text": "Twitter", "next_item": "sm2"}],
            [{"text": "Instagram", "next_item": "sm3"}],
            [{"text": "Geri ⬅️", "next_item": "activity"}],
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
        "1) Psiphon uygulamanızın güncel olduğundan emin olun\n"
        "2) Psiphon en iyi çıkışı bulana kadar bekleyin (bir kaç dakika)\n"
        "3) Psiphon uygulaması üzerinden bize geri bildirim gönderin \n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "Android: Android için Psiphon uygulamasını Google Play Store üzerinden kurduysanız, güncellemeler Play Store tarafından otomatik olarak kurulur. Android için Psiphon uygulamasını başka bir yöntemle kurduysanız, Psiphon güncellemeler yayınlandığında indirir ve kurmanızı isteyen bir bildirim görüntüler.\n\n"
        "Windows: Windows için Psiphon uygulaması yayınlanan güncellemeleri indirir ve kurar.\n\n"
        "iOS: App Store, izin verdiğinizde Psiphon uygulamasını otomatik olarak günceller.",
        "pattern": "f3",
    },
    "share facebook": {
        "message": "Psiphon Facebook hesabını takip edin\n" "https://www.facebook.com/Psiphon-207377692624236/",
        "pattern": "sm1",
    },
    "share twitter": {
        "message": "Psiphon Twitter hesabını takip edin\n" "https://twitter.com/psiphoninc",
        "pattern": "sm2",
    },
    "share instagram": {
        "message": "Psiphon Instagram hesabını takip edin \n" "https://www.instagram.com/psiphoninc/",
        "pattern": "sm3",
    },
}
