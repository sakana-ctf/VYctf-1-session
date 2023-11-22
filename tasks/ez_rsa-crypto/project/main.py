P = 17
Q = 163
E = 7

# 简单的rsa加密技术
N = P * Q
# N = 2771
phin = (P-1) * (Q-1)
D = pow(E, -1, phin)
# print(D)
# D = 1111
PT = open("./flag.ct","w")
with open("./flag.pt","r") as file:
    for f in file.read():
        PT.write(chr((ord(f) ** E) % N))
PT.close()
