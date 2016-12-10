# -*- coding: utf-8 -*-

import base64

a = ['MTIzcGFzc3dvcmQ=',
     'cGFzc3dvcmQ=',
     'MTIzcGFzc3dvcmQ0NQ==',
     'MTIzNDMycGFzc3dvcmQ0NQ==',
     ]

for i in range(4):
    decoded = base64.b64decode(a[i])
    # d = dict.fromkeys(string.ascii_lowercase, i)
    print decoded
print '=========================='

b = ['password',
     '123password',
     '123password45',
     '123pass999word45',
     '123432password45']

for i in range(7):
    encoded = base64.b64encode(b[i])
    decoded = base64.b64decode(encoded)
    print 'EN: ', encoded
    print 'DE: ', decoded
    print
print '=========================='
