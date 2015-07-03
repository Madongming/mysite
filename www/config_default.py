#!/opt/python/bin/python3.4
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Cody Ma'

configs = {
    'debug': False,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-mdm',
        'password': 'www-mdm',
        'db': 'mysite'
    },
    'session': {
        'secret': 'MaDoNgMiNg'
    }
}
