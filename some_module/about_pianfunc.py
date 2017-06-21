# -*- coding: utf-8 -*-

from functools import partial

int2 = partial(int,base=2)

print int2('10010101')
