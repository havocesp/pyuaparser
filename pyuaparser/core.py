#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from typing import Dict

from ua_parser import user_agent_parser

from static import MOBILE_DEVICES, MOBILE_BROWSERS, MOBILE_OS, MUA_APPS, PC_OS, TABLET_DEVICES, TOUCHABLE_OS
from utils import to_int


class BaseItem:
    """Base class"""

    def __init__(self, family):
        self.family = family

    def __str__(self):
        return f'{{{self.family}}}'

    def __repr__(self):
        return self.__str__()


class GenericItem(BaseItem):
    """Base class for OperatingSystem and Browser classes."""

    def __init__(self, **kwargs):
        self.major = kwargs.pop('major')
        self.minor = kwargs.pop('minor')
        self.patch = kwargs.pop('patch')
        super().__init__(kwargs.pop('family'))

    def __str__(self):
        base_class_str = super().__str__().strip('{}')
        return f"{base_class_str}-{self.version_string}"

    @property
    def version(self):
        return [v for v in [self.major, self.minor, self.patch] if v]

    @property
    def version_string(self):
        ver_str = '.'.join(map(str, self.version))
        return '' if ver_str == '.' else ver_str


class Browser(GenericItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OperatingSystem(GenericItem):
    """OS model class for parsed data from User Agent String"""

    def __init__(self, **kwargs):
        self.patch_minor = kwargs.pop('patch_minor')
        super().__init__(**kwargs)


class Device(BaseItem):
    """Device model class for parsed data from User Agent String"""

    def __init__(self, **kwargs):
        self.brand = kwargs.pop('brand')
        self.model = kwargs.pop('model')
        super().__init__(kwargs.pop('family'))


class UserAgent:
    ua_data: Dict
    os: OperatingSystem
    browser: Browser
    device: Device

    def __init__(self, user_agent_str=None):
        self.update(user_agent_str)

    def __str__(self):
        device = 'PC' if self.is_pc else self.device.family
        os = f'{self.os.family} {self.os.version_string}'.strip()
        browser = f'{self.browser.family} {self.browser.version_string}'.strip()
        return '/'.join([device, os, browser])

    def _is_android_tablet(self):
        """Newer Android tablets don't have "Mobile" in their user agent,
        older ones like Galaxy Tab still have "Mobile" though they're not."""
        return 'Mobile Safari' not in self.ua_string and self.browser.family != "Firefox Mobile"

    def _is_blackberry_touch_capable_device(self):
        # A helper to determine whether a BB phone has touch capabilities
        # Blackberry Bold Touch series begins with 99XX
        family = self.device.family
        return 'Blackberry 99' in family or 'Blackberry 95' in family

    @property
    def _families(self):
        return self.os.family, self.device.family, self.browser.family

    @property
    def _versions(self):
        return self.os.version, self.browser.version

    @property
    def _versions_str(self):
        return self.os.version_string, self.browser.version_string

    @property
    def is_tablet(self):
        if self.device.family in TABLET_DEVICES:
            return True
        elif self.os.family == 'Android' and self._is_android_tablet():
            return True
        elif self.os.family == 'Windows' and self.os.version_string.startswith('RT'):
            return True
        elif self.os.family == 'Firefox OS' and 'Mobile' not in self.browser.family:
            return True
        else:
            return False

    @property
    def is_mobile(self, *args):
        dev, browser, os_family = args
        # First check for mobile device and mobile browser families
        if dev in MOBILE_DEVICES or browser in MOBILE_BROWSERS:
            return True
        # Device is considered Mobile OS is Android and not tablet
        # This is not fool proof but would have to suffice for now
        elif (os_family == 'Android' or os_family == 'Firefox OS') and not self.is_tablet:
            return True
        elif os_family == 'BlackBerry OS' and dev != 'Blackberry Playbook':
            return True
        elif os_family in MOBILE_OS:
            return True
        # TODO: remove after https://github.com/tobie/ua-parser/issues/126 is closed
        elif any(s in self.ua_string for s in ('J2ME', 'MIDP')):
            return True
        # This is here mainly to detect Google's Mobile Spider
        elif 'iPhone;' in self.ua_string:
            return True
        elif 'Googlebot-Mobile' in self.ua_string:
            return True
        # Mobile Spiders should be identified as mobile
        elif dev == 'Spider' and 'Mobile' in browser:
            return True
        # Nokia mobile
        elif 'NokiaBrowser' in self.ua_string and 'Mobile' in self.ua_string:
            return True
        else:
            return False

    @property
    def is_touch_capable(self):
        # TODO: detect touch capable Nokia devices
        if any(v in TOUCHABLE_OS for v in self._families):
            return True

        if self.os.family == 'Windows':
            if self.os.version_string.startswith('RT'):
                return True
            if self.os.version_string.startswith('8') and 'Touch' in self.ua_string:
                return True
        if 'BlackBerry' in self.os.family and self._is_blackberry_touch_capable_device():
            return True
        return False

    @property
    def is_pc(self):
        # Returns True for "PC" devices (Windows, Mac and Linux)
        if 'Windows NT' in self.ua_string or self.os.family in PC_OS or \
            self.os.family == 'Windows' and self.os.version_string == 'ME':
            return True
        # TODO: remove after https://github.com/tobie/ua-parser/issues/127 is closed
        if self.os.family == 'Mac OS X' and 'Silk' not in self.ua_string:
            return True
        # Maemo has 'Linux' and 'X11' in UA, but it is not for PC
        if 'Maemo' in self.ua_string:
            return False
        if 'Chrome OS' in self.os.family:
            return True
        if 'Linux' in self.ua_string and 'X11' in self.ua_string:
            return True
        return False

    @property
    def is_bot(self):
        return self.device.family == 'Spider'

    @property
    def is_email_client(self):
        return self.browser.family in MUA_APPS

    def update(self, user_agent):
        if isinstance(user_agent or 0, str) and len(user_agent):
            self.ua_data = user_agent_parser.Parse(user_agent)
            self.ua_data['user_agent'] = {k: to_int(v) for k, v in self.ua_data['user_agent'].items()}
            self.ua_data['os'] = {k: to_int(v) for k, v in self.ua_data['os'].items()}
            self.os = OperatingSystem(**self.ua_data['os'])
            self.browser = Browser(**self.ua_data['user_agent'])
            self.device = Device(**self.ua_data['device'])

    @property
    def ua_string(self):
        return self.ua_data.get('string', '')

    def __repr__(self):
        return str(self)
