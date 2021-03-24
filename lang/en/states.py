states = {
  'activity': {
    'message': "🤖 Welcome to Psiphon's Telegram Bot 🙏",
    'pattern': 'activity',
    'keyboard': [
      [{'text': "Download Psiphon 👻", 'next_item': 'm2' }],
      [{'text': "Frequently Asked Questions 🧐", 'next_item':  'm3' }],
      [{'text': "Social Media 📷", 'next_item': 'm4' }],
    ]
    },
  'os': {
    'message': "🤖 Please select your Operating System 🖥️",
    'pattern': 'm2',
    'keyboard': [
      [{'text': "Windows", 'next_item': 's1' }],
      [{'text': "Android", 'next_item': 's3' }],
      [{'text': "iOS", 'next_item': 's4' }],
      [{'text': "Back ⬅️", 'next_item': 'activity' }],
    ]
    },
  'faq': {
    'message': "🤖 Please select your question",
    'pattern': 'm3',
    'keyboard': [
      [{'text': "Psiphon does not work", 'next_item': 'f1' }],
      [{'text': "How do I update Psiphon?", 'next_item': 'f3' }],
      [{'text': "I have a different question", 'next_item': 'f2' }],
      [{'text': "Back ⬅️", 'next_item': 'activity' }],
    ]
    },
  'social': {
    'message': "Follow Psiphon",
    'pattern': 'm4',
    'keyboard': [
      [{'text': "Facebook", 'next_item': 'sm1' }],
      [{'text': "Twitter", 'next_item': 'sm2' }],
      [{'text': "Instagram", 'next_item': 'sm3' }],
      [{'text': "Back ⬅️", 'next_item': 'activity' }],
    ]
    },
    'windows download': {
      'message': 'https://s3.amazonaws.com/psiphon/web/mmqu-p8qj-sgdq/psiphon3.exe',
      'pattern': 's1',
    },
    'android download': {
      'message': 'https://s3.amazonaws.com/psiphon/web/mmqu-p8qj-sgdq/PsiphonAndroid.apk' ,
      'pattern': 's3',
    },
    'ios download': {
      'message': 'https://itunes.apple.com/app/psiphon/id1276263909?ls=1&mt=8',
      'pattern': 's4',
    },
    'faq q1': {
      'message': ''
                 '1) Make sure your Psiphon client is updated.\n'
                 '2) Wait for (up to a few minutes) until Psiphon finds the best way out\n'
                 '3) Send us feedback through the Psiphon\'s app\n',
      'pattern': 'f1',
    },
    'faq q2': {
      'message': 'https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html',
      'pattern': 'f2',
    },
    'faq q3': {
      'message': 'Android: If you have installed Psiphon for Android through the Google Play Store, it will be automatically updated by the Play Store when an update is available. If you have sideloaded Psiphon for Android, the Psiphon client will download updates as they are available, and a notification will appear asking you to install the update.\n\n' 
                 'Windows: The Psiphon for Windows client will download and install updates as they are available.\n\n'
                 'iOS: App Store atumatically updates Psiphon, when you permit it.',
      'pattern': 'f3',
    },
    'share facebook': {
      'message': 'Follow Psiphon on Facebook \n'
                 'https://www.facebook.com/Psiphon-207377692624236/',
      'pattern': 'sm1',
    },
    'share twitter': {
      'message': 'Follow Psiphon on Twitter \n'
                 'https://twitter.com/psiphoninc',
      'pattern': 'sm2',
    },
    'share instagram': {
      'message': 'Follow Psiphon on Instagram \n'
                 'https://www.instagram.com/psiphoninc/',
      'pattern': 'sm3',
    },
  }
