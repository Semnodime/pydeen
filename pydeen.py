#!/usr/bin/env python3
import sys
from codecs import decode, encode
data = sys.stdin.read()[:-1]
print(encode(decode(data, sys.argv[1]), sys.argv[2]).decode())
