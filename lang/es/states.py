states = {
    "activity": {
        "message": "🤖 Bienvenido al chatbot de Telegram de Psiphon 🙏",
        "pattern": "activity",
        "keyboard": [
            [{"text": "Descargar Psiphon 👻", "next_item": "m2"}],
            [{"text": "Preguntas Frecuentes 🧐", "next_item": "m3"}],
            [{"text": "Redes sociales 📷", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "🤖 Por favor, selecciona tu Sistema Operativo 🖥️",
        "pattern": "m2",
        "keyboard": [
            [{"text": "Windows", "next_item": "s1"}],
            [{"text": "Android", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "Regresar ⬅️", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "🤖 Por favor, selecciona tu pregunta",
        "pattern": "m3",
        "keyboard": [
            [{"text": "Psiphon no funciona", "next_item": "f1"}],
            [{"text": "¿Cómo actualizo Psiphon?", "next_item": "f3"}],
            [{"text": "Tengo una pregunta diferente", "next_item": "f2"}],
            [{"text": "Regresar ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "Seguir a Psiphon en las redes sociales",
        "pattern": "m4",
        "keyboard": [
            [{"text": "Facebook", "next_item": "sm1"}],
            [{"text": "Twitter", "next_item": "sm2"}],
            [{"text": "Instagram", "next_item": "sm3"}],
            [{"text": "Regresar ⬅️", "next_item": "activity"}],
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
        "1) Asegúrate de que tu aplicación Psiphon esté actualizada.\n"
        "2) Espera unos minutos a que Psiphon encuentre la mejor solución. \n"
        "3) Envíanos tus comentarios a través de la aplicación Psiphon. \n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "Android: Si has instalado Psiphon para Android a través de la Google Play Store, será actualizado automáticamente cuando una actualización esté disponible. Si lo has hecho desde otro sitio, la aplicación Psiphon descargará las actualizaciones en la medida en que estén disponibles, y aparecerá una notificación solicitándote instalarlas.\n\n"
        "Windows: La aplicación de Psiphon para Windows descargará e instalará actualizaciones en la medida en que estén disponibles. \n\n"
        "iOS: App Store automáticamente actualiza a Psiphon, cuando lo permites.",
        "pattern": "f3",
    },
    "share facebook": {
        "message": "Sigue a Psiphon en Facebook \n" "https://www.facebook.com/Psiphon-Espa%C3%B1ol-1150535835035919/",
        "pattern": "sm1",
    },
    "share twitter": {
        "message": "Sigue a Psiphon en Twitter \n" "https://twitter.com/psiphonesp",
        "pattern": "sm2",
    },
    "share instagram": {
        "message": "Sigue a Psiphon en Instagram \n" "https://www.instagram.com/psiphon_es/",
        "pattern": "sm3",
    },
}
