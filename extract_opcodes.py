#!/usr/bin/env python2.7
# coding: UTF-8

from __future__ import print_function

begin_addr = 0x0000000001000058
end_addr = 0x0000000001000063

print('opcodes: ', end='')
for i in range(begin_addr, end_addr+1):
    print(format(idc.Byte(i), '02x'), end='')
print('')
