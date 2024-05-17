states = {
    "activity": {
        "message": "🤖به ربات تلگرامی سایفون خوش‌آمدید 👋",
        "pattern": "activity",
        "keyboard": [
            [{"text": "دانلود سایفون 👻", "next_item": "m2"}],
            [{"text": "پرسش‌های متداول 🧐", "next_item": "m3"}],
            [{"text": "رسانه‌های اجتماعی 📷", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "🤖لطفا سیستم عامل خود را انتخاب کنید 🖥️",
        "pattern": "m2",
        "keyboard": [
            [{"text": "ویندوز", "next_item": "s1"}],
            [{"text": "اندروید", "next_item": "s3"}],
            [{"text": "آی‌او‌اس", "next_item": "s4"}],
            [{"text": "بازگشت ⬅️ ", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "🤖سوال مورد نظر را انتخاب کنید",
        "pattern": "m3",
        "keyboard": [
            [{"text": "سایفون وصل نمی‌شود، چه کنم؟", "next_item": "f1"}],
            [{"text": "سایفون را چطور به روز کنم؟", "next_item": "f2"}],
            [{"text": "سوال دیگری دارم", "next_item": "f3"}],
            [{"text": "بازگشت ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "سایفون را دنبال کنید",
        "pattern": "m4",
        "keyboard": [
            [{"text": "توییتر", "next_item": "sm1"}],
            [{"text": "اینستاگرام", "next_item": "sm2"}],
            [{"text": "تلگرام", "next_item": "sm3"}],
            [{"text": "وب‌سایت", "next_item": "sm4"}],
            [{"text": "بازگشت ⬅️", "next_item": "activity"}],
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
        "اول ) مطمئن شوید از آخرین نسخه سایفون استفاده می‌کنید\n"
        "دوم) تا چند دقیقه به سایفون وقت دهید تا بهترین مسیر را پیدا کند\n"
        "سوم) از طریق اپ سایفون برای ما «فیدبک» یا «بازخورد» بفرستید.\n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/fa/faq.html",
        "pattern": "f3",
    },
    "faq q3": {
        "message": "اندروید: اگر شما نسخه‌ی اندروید سایفون را از گوگل پلی استور نصب کرده‌اید، به صورت خودکار و هنگامی که پلی‌استور نسخه‌ی جدیدتری داشته باشد به روز می‌شود. اگر سایفون اندروید را نصب کرده‌اید، سایفون تغییرات به‌روزرسانی را دانلود می‌کند و پیش از نصب برای گرفتن مجوز از شما سوال می‌کند.\n\n"
        " ویندوز: سایفون ویندوز تغییرات به‌روزرسانی موجود را دانلود و نصب می‌کند.\n\n"
        " آی‌او‌اس: اپل‌استور به صورت خودکار یا با کسب اجازه از شما سایفون را به روز می‌کند.",
        "pattern": "f2",
    },
    "share twitter": {
        "message": "https://twitter.com/psiphon_fa",
        "pattern": "sm1",
    },
    "share instagram": {
        "message": "https://www.instagram.com/psiphon_fa/",
        "pattern": "sm2",
    },
    "share Telegram": {
        "message": "https://t.me/Psiphon_F",
        "pattern": "sm3",
    },
    "share website": {
        "message": "https://psiphon.ca/",
        "pattern": "sm4",
    },
}
