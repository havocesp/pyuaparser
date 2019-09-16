# PyUAParser

A pure Python User Agent parser.

 - Author: Daniel J. Umpierrez
 - License: UNLICENSE
 - Version: 0.1.0

## Description

Parse a User Agent raw string and parse it to a Operative System, Device, and Browser objects. 

## Requirements

 - [ua-parser](https://pypi.org/project/ua-parser)

## Installation
```sh
    pip install git+https://github.com/havocesp/pyuaparser
```

## Usage

### Basic example

```python
from pyuaparser import UserAgent

if __name__ == '___main__':
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    ua = UserAgent(user_agent)
    print(ua)  # prints: PC/Windows 10/Chrome 60.3112
    print(ua.os.family)  # prints: Windows
    print(ua.os.major)  # prints: 10
```

## Changelog

Project changes over versions.

### 0.1.0
- Initial version
