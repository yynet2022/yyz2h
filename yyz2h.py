# -*- coding:utf-8 -*-
import sys
import os
import pathlib
import tempfile
import chardet

ZN = ''.join(chr(0xff01 + i) for i in range(94)) + '　'
HN = ''.join(chr(0x21 + i) for i in range(94)) + ' '
Z2H = str.maketrans(ZN, HN)
# print(s.translate(Z2H))

for f in sys.argv[1:]:
    try:
        with open(f, 'rb') as rfd:
            b = rfd.read()
            c = chardet.detect(b)
            # print(c)
            ln = b.decode(c['encoding'])

            p = pathlib.PurePath(f)
            (wfd, n) = tempfile.mkstemp(
                suffix='_' + p.name, prefix='z2h_', dir=p.parent)

            os.write(wfd, ln.translate(Z2H).encode('utf-8'))
            os.close(wfd)
    except Exception as e:
        print(str(e))
