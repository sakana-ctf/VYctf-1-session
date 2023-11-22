# sage部分代码
from sage.all import *
import hashlib
P = Permutations(8).random_element()
print("P的平方为:",P**2)
# python部分代码
print("加密结果为:",[x^y for x,y in zip(hashlib.sha512(str(P).encode()).digest(), open('flag.txt', 'rb').read())])

