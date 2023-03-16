import sys
from pprint import pprint

from utils import *
from models import *

print(list(filter(lambda str: not ("__" in str), dir())))
# print(dir())
# print(__name__)
# pprint(sys.path)
