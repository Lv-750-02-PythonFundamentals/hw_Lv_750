# from module01 import my_funk, a, my_mane, _my_mane, __my_mane
from  module01 import *
print(dir())

import module01
module01.__my_mane()