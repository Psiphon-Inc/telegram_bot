states = {
  'activity': {
    'message': "🤖 Baga Telegram Bot Psiphon'ii nagan dhuftan",
    'pattern': 'activity',
    'keyboard': [
      [{'text': "Psiphon gad fe'adhaa", 'next_item': 'm2' }],
      [{'text': "Gafiwwan deddebiin gafataman", 'next_item':  'm3' }],
      [{'text': "Midiiyaa hawaasaa", 'next_item': 'm4' }],
    ]
    },
  'os': {
    'message': "Mee seera ittin shakaltan filadhaa",
    'pattern': 'm2',
    'keyboard': [
      [{'text': "Windows", 'next_item': 's1' }],
      [{'text': "Android", 'next_item': 's3' }],
      [{'text': "iOS", 'next_item': 's4' }],
      [{'text': "Deebi'i ⬅️", 'next_item': 'activity' }],
    ]
    },
  'faq': {
    'message': "Mee gaafii keesaan filadhaa",
    'pattern': 'm3',
    'keyboard': [
      [{'text': "Psiphon Hin hojjatu", 'next_item': 'f1' }],
      [{'text': "Akkamittan Psiphon foyyeffachu danda'a?", 'next_item': 'f3' }],
      [{'text': "Gaafii biraa qaba", 'next_item': 'f2' }],
      [{'text': "Deebi'i ⬅️", 'next_item': 'activity' }],
    ]
    },
  'social': {
    'message': "Psiphon hordofi",
    'pattern': 'm4',
    'keyboard': [
      [{'text': "Facebook", 'next_item': 'sm1' }],
      [{'text': "Twitter", 'next_item': 'sm2' }],
      [{'text': "Instagram", 'next_item': 'sm3' }],
      [{'text': "Deebi'i ⬅️", 'next_item': 'activity' }],
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
                 '1) Maalimni Psiphon keessaan Foyyeeffamusaa beeki.\n'
                 '2) Psiphon karaa bahinsaa gaari hanga argatutti xiqqoo eegaa.\n'
                 '3) Fayyadama Psiphon iin dubdeebii nu ergaa.\n',
      'pattern': 'f1',
    },
    'faq q2': {
      'message': 'https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html',
      'pattern': 'f2',
    },
    'faq q3': {
      'message': "Android: Android Psiphon, Google play store irra yoo fe'atan yeroo Foyyefamni jiraate Play store dhan bakkumati fayyefama.\n\n"
                 "Windows: foyyeffamni jiratan maalima windowsiif Psiphoniin hinfe'amaaf.\n\n"
                 'iOS: Yeroo eeyyamtan App Store bakkumatti Psiphon fooyyessa.',
      'pattern': 'f3',
    },
    'share facebook': {
      'message': 'Psiphon Facebook irratti hordoofaa \n'
                 'https://www.facebook.com/Psiphon-207377692624236/',
      'pattern': 'sm1',
    },
    'share twitter': {
      'message': 'Psiphon Twitter irratti hordofaa \n'
                 'https://twitter.com/psiphoninc',
      'pattern': 'sm2',
    },
    'share instagram': {
      'message': 'Instagram irratti hordofaa\n'
                 'https://www.instagram.com/psiphoninc/',
      'pattern': 'sm3',
    },
  }