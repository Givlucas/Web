#!/usr/bin/python
# -*- coding: utf-8 -*-
import six
import socket, sys

if len(sys.argv) < 2:
        sys.exit(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("192.168.1.75", 6020))

freq = int(sys.argv[1])

print(freq)
buf = b"A"*268

while freq > 0:
        buf = buf + chr(freq & 0xff)
        freq = freq >> 8
print(bytes(buf, 'utf8'))
s.send(six.b(buf))
s.close()
