"""
my module02
"""

print(dir())
print(__doc__)
import module01

print(module01.__doc__)
a = 10
print(module01.a)
module01.my_funk()
print(a)

# from module01 import *
from module01 import a as aa, my_funk as mf

print(a)
mf()
print(aa)

import module01 as m01

a = 10
print(m01.a)
m01.my_funk()
print(a)
print(id(module01), module01)
print(id(m01), m01)
print(dir())

print("module name: ", __name__)

import math

print(math.__name__)
# from lesson09 import lesson07

import sys

sys.path.append('C:\\data\\github\\hw_Lv_750')
from lesson07 import lesson07

print(lesson07)

from a.b.c import d

print(d)

if __name__ == "__main__":
    print("foo")

from pprint import pprint

pprint(sys.path)

def fu():
    import math as t
    print(t.sin(10))

