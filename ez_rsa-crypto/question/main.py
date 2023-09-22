def xgcd(a, b):
    """
    扩展欧几里得GCD算法.
    返还(x, y, g)满足以下数学关系 : a * x + b * y = g, 
    其中gcd(a, b) = a * x + b * y
    """
    if a == 0:
        return 0, 1, b
    if b == 0:
        return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a

def invmod(a, n):
    """
    求逆膜法, 返还 1 / a (mod n).
    其中a和n需要互质
    """
    if n < 2:
        raise ValueError("求膜必须使n大于1!")

    x, y, g = xgcd(a, n)

    if g != 1:
        raise ValueError("给定的a与n没有逆膜!")
    else:
        return x % n

# 简单的rsa加密技术
E = 7
N = P * Q
# N = 2771
phin = (P-1) * (Q-1)
D = invmod(E, phin)
# print(D)
# D = 1111
PT = open("./flag.ct","w")
with open("./flag.pt","r") as file:
    for f in file.read():
        PT.write(chr((ord(f) ** E) % N))
PT.close()