states = {
    "activity": {
        "message": "🤖اهلا بكم في سايفون بوت عبر تليغرام 🙏",
        "pattern": "activity",
        "keyboard": [
            [{"text": "حمل سايفون 👻", "next_item": "m2"}],
            [{"text": "الأسئلة الشائعة 🧐", "next_item": "m3"}],
            [{"text": "وسائل التواصل الاجتماعي 📷", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "🤖حدد نظام التشغل الخاص بك 🖥️",
        "pattern": "m2",
        "keyboard": [
            [{"text": "ویندوز", "next_item": "s1"}],
            [{"text": "اندروید", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "العودة ⬅️", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "🤖حدد السؤال",
        "pattern": "m3",
        "keyboard": [
            [{"text": "سايفون لم يتصل ، ماذا أفعل؟'", "next_item": "f1"}],
            [{"text": "كيفية تحديث سايفون؟", "next_item": "f3"}],
            [{"text": "لدي سؤال مختلف", "next_item": "f2"}],
            [{"text": "العودة ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "تابعوا سايفون",
        "pattern": "m4",
        "keyboard": [
            [{"text": "فیسبوک", "next_item": "sm1"}],
            [{"text": "توییتر", "next_item": "sm2"}],
            [{"text": "انستغرام", "next_item": "sm3"}],
            [{"text": "العودة ⬅️", "next_item": "activity"}],
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
        "1) تأكد من تحديث تطبيق سايفون الخاص بك\n"
        "2) انتظر (بضع دقائق) حتى يجد سايفون أفضل وسيلة للاتصال\n"
        "3) أرسل لنا ملاحظاتك من خلال تطبيق سايفون\n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/ar/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "اندرويد: إذا قمت بتثبيت سايفون على نظام اندرويد من خلال متجر غوغل، فسيتم تحديثه تلقائيًا بواسطة المتجر عندما يتوفر اي تحديث. إذا قمت بتحميل سايفون على نظام اندرويد ، فإن عميل سايفون سينزل التحديثات بمجرد توفرها، وسيظهر إشعار يطلب منك تثبيت التحديث.\n\n"
        "ويندوز: سيقوم عميل سايفون على ويندوز بتنزيل التحديثات وتثبيتها حال توفرها.\n\n"
        "ايفون: يقوم متجر آبل بتحديث سايفون تلقائيًا بعد أخذ الأذونات المطلوبة",
        "pattern": "f3",
    },
    "share facebook": {
        "message": "سايفون على فيسبوك \n" "https://www.facebook.com/PsiphonArabic/",
        "pattern": "sm1",
    },
    "share twitter": {
        "message": "سايفون على تويتر \n" "https://twitter.com/PsiphonArabic",
        "pattern": "sm2",
    },
    "share instagram": {
        "message": "سايفون على انستاغرام \n" "https://www.instagram.com/Psiphon_Ar/",
        "pattern": "sm3",
    },
}
