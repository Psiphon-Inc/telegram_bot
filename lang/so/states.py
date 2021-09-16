states = {
  'activity': {
    'message': "🤖 Ku soo dhowow Psiphon's Telegram Bot",
    'pattern': 'activity',
    'keyboard': [
      [{'text': "Soo dejiso Psiphon", 'next_item': 'm2' }],
      [{'text': "Su'aalaha Badanaa La Is Weydiiyo", 'next_item':  'm3' }],
      [{'text': "Warbaahinta bulshada", 'next_item': 'm4' }],
    ]
    },
  'os': {
    'message': "Fadlan dooro Nidaamkaaga Howlgalka",
    'pattern': 'm2',
    'keyboard': [
      [{'text': "Windows", 'next_item': 's1' }],
      [{'text': "Android", 'next_item': 's3' }],
      [{'text': "iOS", 'next_item': 's4' }],
      [{'text': "Dib u laabo ⬅️", 'next_item': 'activity' }],
    ]
    },
  'faq': {
    'message': "Fadlan xulo su'aashaada",
    'pattern': 'm3',
    'keyboard': [
      [{'text': "Psiphon ma shaqeeyo", 'next_item': 'f1' }],
      [{'text': "Sideen u cusbooneysiiyaa Psiphon?", 'next_item': 'f3' }],
      [{'text': "Waxaan qabaa su'aal ka duwan", 'next_item': 'f2' }],
      [{'text': "Dib u laabo ⬅️", 'next_item': 'activity' }],
    ]
    },
  'social': {
    'message': "FRaac Psiphon",
    'pattern': 'm4',
    'keyboard': [
      [{'text': "Facebook", 'next_item': 'sm1' }],
      [{'text': "Twitter", 'next_item': 'sm2' }],
      [{'text': "Instagram", 'next_item': 'sm3' }],
      [{'text': "Dib u laabo ⬅️", 'next_item': 'activity' }],
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
                 '1) Hubso in macmiilkaaga Psiphon la cusbooneysiiyay.\n'
                 '2) Sug (illaa daqiiqado) illaa Psiphon ka helayo habka ugu wanaagsan ee looga baxo.\n'
                 "3) Noo soo dir ra'yi-celinta barnaamijka Psiphon.\n",
      'pattern': 'f1',
    },
    'faq q2': {
      'message': 'https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html',
      'pattern': 'f2',
    },
    'faq q3': {
      'message': 'Android: Haddii aad ku rakibtay Psiphon for Android adoo adeegsanaya Google Play Store, waxaa si toos ah u cusbooneysiin doonaa Play Store marka cusbooneysi la heli karo. Haddii aad dhinac ka buuxisay Psiphon loogu talagalay Android, macmiilka Psiphon wuxuu soo dejinayaa cusbooneysiinta sida ay diyaar u yihiin, ogeysiis ayaa kuu muuqan doona oo kaa codsanaya inaad cusbooneysiiso cusbooneysiinta.\n\n' 
                 'Windows: Psiphon ee macaamilka Windows ayaa soo dejisan doona oo rakibi doona cusbooneysiinta maaddaama ay diyaar yihiin.\n\n'
                 'iOS:App Store si otomaatig ah ayuu u cusbooneysiiyaa Psiphon, markaad u oggolaato.',
      'pattern': 'f3',
    },
    'share facebook': {
      'message': 'Raac Psiphon Facebook \n'
                 'https://www.facebook.com/Psiphon-207377692624236/',
      'pattern': 'sm1',
    },
    'share twitter': {
      'message': 'Raac Psiphon barta Twitter \n'
                 'https://twitter.com/psiphoninc',
      'pattern': 'sm2',
    },
    'share instagram': {
      'message': 'Raac Psiphon barta Instagram \n'
                 'https://www.instagram.com/psiphoninc/',
      'pattern': 'sm3',
    },
  }