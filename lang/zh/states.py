states = {
    "activity": {
        "message": "🤖欢迎来到赛风的电报机器人",
        "pattern": "activity",
        "keyboard": [
            [{"text": "下载赛风 👻", "next_item": "m2"}],
            [{"text": "常见问题 🧐", "next_item": "m3"}],
            [{"text": "社交媒体 📷", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "🤖请选择你的操作系统 🖥️",
        "pattern": "m2",
        "keyboard": [
            [{"text": "Windows", "next_item": "s1"}],
            [{"text": "Android", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "返回 ⬅️", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "🤖请选择你的问题",
        "pattern": "m3",
        "keyboard": [
            [{"text": "赛风不能正常连接，我该怎么做？", "next_item": "f1"}],
            [{"text": "如何更新赛风?", "next_item": "f3"}],
            [{"text": "为什么我不能从App Store下载赛风?", "next_item": "f4"}],
            [{"text": "我有其他问题。", "next_item": "f2"}],
            [{"text": "返回 ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "请在社交媒体上关注赛风",
        "pattern": "m4",
        "keyboard": [
            [{"text": "Twitter", "next_item": "sm1"}],
            [{"text": "Instagram", "next_item": "sm2"}],
            [{"text": "返回 ⬅️", "next_item": "activity"}],
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
        "1) 请确保您的赛风客户端是最新的版本。\n"
        "2) 链接时请等待几分钟从而让赛风找到最优化的路径。\n"
        "3) 请通过赛风客户端给我们发送反馈。\n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/zh/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "Android： 如果您从谷歌Play Store下载安装赛风Android客户端，该客户端会在新版本发布于Play Store时自动更新。如果您从其他渠道下载安装赛风Android客户端，赛风客户端会及时下载更新，并提示您安装下载好的更新。\n\n"
        "赛风Windows客户端会在更新发布的第一时间，自动下载并安装更新。\n\n"
        "iOS：当您允许时，App Store会自动更新赛风客户端。",
        "pattern": "f3",
    },
    "faq q4": {
        "message": "根据法律规定，赛风在大陆App商店不适用，所以您需使用非大陆地区的Apple账号来下载赛风。",
        "pattern": "f4",
    },
    "share facebook": {
        "message": "https://twitter.com/PsiphonChina",
        "pattern": "sm1",
    },
    "share twitter": {
        "message": "https://www.instagram.com/psiphon_cn",
        "pattern": "sm2",
    },
}
