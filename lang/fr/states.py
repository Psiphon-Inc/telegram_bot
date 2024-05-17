states = {
    "activity": {
        "message": "🤖 Bienvenue au chatbot",
        "pattern": "activity",
        "keyboard": [
            [{"text": "Téléchargez Psiphon", "next_item": "m2"}],
            [{"text": "Foire aux questions", "next_item": "m3"}],
            [{"text": "Médias sociaux", "next_item": "m4"}],
        ],
    },
    "os": {
        "message": "Veuillez choisir votre système d'exploitation",
        "pattern": "m2",
        "keyboard": [
            [{"text": "Windows", "next_item": "s1"}],
            [{"text": "Android", "next_item": "s3"}],
            [{"text": "iOS", "next_item": "s4"}],
            [{"text": "Retour ⬅️", "next_item": "activity"}],
        ],
    },
    "faq": {
        "message": "Veuillez sélectionner votre question",
        "pattern": "m3",
        "keyboard": [
            [{"text": "Psiphon ne fonctionne pas", "next_item": "f1"}],
            [{"text": "Comment puis-je mettre Psiphon à jour?", "next_item": "f3"}],
            [{"text": "J'ai une question différente", "next_item": "f2"}],
            [{"text": "Retour ⬅️", "next_item": "activity"}],
        ],
    },
    "social": {
        "message": "Suivez Psiphon",
        "pattern": "m4",
        "keyboard": [
            [{"text": "Facebook", "next_item": "sm1"}],
            [{"text": "Twitter", "next_item": "sm2"}],
            [{"text": "Instagram", "next_item": "sm3"}],
            [{"text": "Retour ⬅️", "next_item": "activity"}],
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
        "1) Assurez-vous que votre client est à jour.\n"
        "2) Patientez (peut-être quelques minutes) jusqu'à ce que Psiphon trouve le meilleur chemin de sortie.\n"
        "3) Envoyez-nous une rétroaction avec l'application Psiphon.\n",
        "pattern": "f1",
    },
    "faq q2": {
        "message": "https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html",
        "pattern": "f2",
    },
    "faq q3": {
        "message": "Android: si vous avez installé Psiphon pour Android au magasin Google «Play Store» , l'appli sera mise à jour automatiquement par «Play Store» si une mise à jour est proposée. Si vous avez opté pour un téléchargement hors magasin de Psiphon pour Android, le clientPsiphon téléchargera la mise à jour quand elle sera proposée et une notification apparaîtra vous demandant d'installer la mise à jour.\n\n"
        "Windows: le client Psiphon pour Windows téléchargera et installera les mises à jour quand elles seront proposées.\n\n"
        "iOS: le magasin d'applications «App Store» met Psiphon à jour automatiquement, si vous l'autorisez.",
        "pattern": "f3",
    },
    "share facebook": {
        "message": "Suivez Psiphon sur Facebook \n" "https://www.facebook.com/Psiphon-207377692624236/",
        "pattern": "sm1",
    },
    "share twitter": {
        "message": "Suivez Psiphon sur Twitter \n" "https://twitter.com/psiphoninc",
        "pattern": "sm2",
    },
    "share instagram": {
        "message": "Suivez Psiphon sur Instagram \n" "https://www.instagram.com/psiphoninc/",
        "pattern": "sm3",
    },
}
