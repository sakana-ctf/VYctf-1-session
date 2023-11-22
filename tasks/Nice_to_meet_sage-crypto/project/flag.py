import hashlib
P = [3, 7, 5, 1, 4, 6, 8, 2]
print("加密结果为:",[x^y for x,y in zip(hashlib.sha512(str(P).encode()).digest(), open('flag.txt', 'rb').read())])
