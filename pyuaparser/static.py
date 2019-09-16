# -*- coding:utf-8 -*-

PC_OS = [
    'Windows 95',
    'Windows 98',
    'Windows ME',
    'Windows XP',
    'Windows 10',
    'Windows 8',
    'Windows 8.1',
    'Windows 7',
    'Windows 2000',
    'Windows NT',
    'Solaris',
    'Linux'
]

MOBILE_DEVICES = [
    'iPhone',
    'iPod',
    'Generic Smartphone',
    'Generic Feature Phone',
    'PlayStation Vita',
    'iOS-Device',
    'J2ME',
    'MIDP',
    'Spider',
    'Googlebot-Mobile'
]

MOBILE_OS = [
    'Windows Phone',
    'Windows Phone OS',  # Earlier versions of ua-parser returns Windows Phone OS
    'Symbian OS',
    'Bada',
    'Windows CE',
    'Windows Mobile',
    'Maemo'
]

MOBILE_BROWSERS = [
    'Opera Mobile',
    'Opera Mini',
    'NokiaBrowser'
]

TABLET_DEVICES = [
    'iPad',
    'BlackBerry Playbook',
    'Blackberry Playbook',  # Earlier versions of ua-parser returns "Blackberry" instead of "BlackBerry"
    'Kindle',
    'Kindle Fire',
    'Kindle Fire HD',
    'Galaxy Tab',
    'Xoom',
    'Dell Streak',
]

TOUCHABLE_OS = [
    'iOS',
    'Android',
    'Windows Phone',
    'Windows CE',
    'Windows Mobile',
    'Firefox OS',
    'MeeGo'
]

TOUCHABLE_DEVICES = [
    'BlackBerry Playbook',
    'Blackberry Playbook',
    'Kindle Fire'
]

MUA_APPS = {
    'Outlook',
    'Windows Live Mail',
    'AirMail',
    'Apple Mail',
    'Outlook',
    'Thunderbird',
    'Lightning',
    'ThunderBrowse',
    'Windows Live Mail',
    'The Bat!',
    'Lotus Notes',
    'IBM Notes',
    'Barca',
    'MailBar',
    'kmail2',
    'YahooMobileMail'
}

ALL_TOUCHABLE = TOUCHABLE_OS + TOUCHABLE_DEVICES
ALL_MOBILES = MOBILE_OS + MOBILE_BROWSERS + MOBILE_DEVICES
ALL_DEVICES = MOBILE_DEVICES + TABLET_DEVICES + TABLET_DEVICES
ALL_OS = TOUCHABLE_OS + MOBILE_OS + PC_OS
