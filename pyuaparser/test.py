# -*- coding:utf-8 -*-
from core import UserAgent

testing_data = {
    'user_agent': {
        'family': 'Chrome',
        'major': '60',
        'minor': '0',
        'patch': '3112'
    },
    'os': {
        'family': 'Windows',
        'major': '10',
        'minor': None,
        'patch': None,
        'patch_minor': None
    },
    'device': {
        'family': 'Other',
        'brand': None,
        'model': None
    },
    'string': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

ua = UserAgent(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
ua2 = UserAgent(
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')

print(ua)
print(ua2)
