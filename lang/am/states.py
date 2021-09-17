states = {
  'activity': {
    'message': "🤖 እንኳን በደህና ወደ Telegram (ቴሌግራም) ቦት በደህና መጡ",
    'pattern': 'activity',
    'keyboard': [
      [{'text': "Psiphonን አውርድ", 'next_item': 'm2' }],
      [{'text': "በተደጋጋሚ የሚጠየቁ ጥያቄዎች", 'next_item':  'm3' }],
      [{'text': "ማሕበራዊ ሚዲያ", 'next_item': 'm4' }],
    ]
    },
  'os': {
    'message': "እባክዎትን ሥርዓተ ክዋኔዎን  ይምረጡ",
    'pattern': 'm2',
    'keyboard': [
      [{'text': "Windows (ዊንዶውስ)", 'next_item': 's1' }],
      [{'text': "Android (አንድሮይድ)", 'next_item': 's3' }],
      [{'text': "iOS (አይ ኦ ኤስ)", 'next_item': 's4' }],
      [{'text': "ተመለስ ⬅️", 'next_item': 'activity' }],
    ]
    },
  'faq': {
    'message': "እባክዎትን ጥያቄዎትን ይምረጡ",
    'pattern': 'm3',
    'keyboard': [
      [{'text': "Psiphon አይሠራም", 'next_item': 'f1' }],
      [{'text': "Psiphonን እንዴት ነው የማዘምነው？", 'next_item': 'f3' }],
      [{'text': "ሌላ ጥያቄ አለኝ", 'next_item': 'f2' }],
      [{'text': "ተመለስ ⬅️", 'next_item': 'activity' }],
    ]
    },
  'social': {
    'message': "Psiphonን ተከተል",
    'pattern': 'm4',
    'keyboard': [
      [{'text': "Facebook (ፌስቡክ)", 'next_item': 'sm1' }],
      [{'text': "Twitter (ትዊተር)", 'next_item': 'sm2' }],
      [{'text': "Instagram (ኢንስታግራም)", 'next_item': 'sm3' }],
      [{'text': "ተመለስ ⬅️", 'next_item': 'activity' }],
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
                 '1) የእርስዎ Psiphon ተገልጋይ እንደተዘመነ ያረጋግጡ።\n'
                 '2) Psiphon ከሁሉ የተሻለውን መውጫ እስኪያገኝ ድረስ ይጠብቁ (ለጥቂት ደቂቃዎች ያህል)\n'
                 '3) በPsiphon መተግበሪያ በኩል ግብረመልስ ይላኩልን\n',
      'pattern': 'f1',
    },
    'faq q2': {
      'message': 'https://s3.amazonaws.com/psiphon/web/6rcw-62xy-i1zw/en/faq.html',
      'pattern': 'f2',
    },
    'faq q3': {
      'message': 'Android: Psiphon ለAndroidን በGoogle Play Store አማካኝነት ከጫኑ፤ ዝመና ሲኖር Play Store በራስ-ሰር ያዘምነዋል። የAndroid Psiphonን ከሌላ ቦታ አውርደው ከጫኑ የPsiphon መተግበሪያው ዝመናዎችን እንደተገኙ አውርዶ ዝመናውን እንዲጭኑ የሚጠይቅ ማሳወቂያ ያመጣል።\n\n' 
                 'Windows፡ Psiphon ለWindows ደንበኛው ዝመናዎችን እንደተገኙ አውርዶ ይጭናል።\n\n'
                 'iOS፡ ለApp Store ፈቃድ ሲሰጡት Psiphonን በራስ ሰር ያዘምናል።',
      'pattern': 'f3',
    },
    'share facebook': {
      'message': 'Psiphonን Facebook (ፌስቡክ) ላይ \n'
                 'https://www.facebook.com/Psiphon-207377692624236/',
      'pattern': 'sm1',
    },
    'share twitter': {
      'message': 'Psiphonን Twitter (ትዊተር) ላይ \n'
                 'https://twitter.com/psiphoninc',
      'pattern': 'sm2',
    },
    'share instagram': {
      'message': 'Psiphonን Instagram (ኢንስታግራም) ላይ\n'
                 'https://www.instagram.com/psiphoninc/',
      'pattern': 'sm3',
    },
  }