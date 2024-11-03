from script import *
import sys
import hashlib

#incorpated module
import math

print(div(1, 3))

#lists all the available functions
print(dir(math))

#list built-in modules
print(sys.builtin_module_names)

#not built-in modules
print(hashlib.md5(b"hi!").hexdigest())

print(hashlib.__file__)