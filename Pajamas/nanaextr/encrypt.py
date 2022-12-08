# -*- coding:utf-8 -*-

import struct

src = open('dltextdata.bin', 'rb')

dst = open('en_textdata.bin', 'wb')

#即CL
key = 0xc5

#计算size
src.seek(0,2)
size = src.tell()
src.seek(0)

for i in range(0, size):
    unstr = src.read(1)[0]
    destr = unstr ^ key
    key += 0x5c
    key &= 0xff
    dst.write(bytes([destr]))

src.close()
dst.close()
