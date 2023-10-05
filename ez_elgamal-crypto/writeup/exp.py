P = 487
# D = ?
E1 = 31
#E2 = pow(E1, D, P)
E2 = 168
R = 11

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

def enc(PT, E1, E2, R, P):
    C1 = pow(E1, R, P)
    C2 = ""
    for i in PT:
        data = (i * pow(E2, R)) % P
        C2 += chr(data)
    return C1,C2

def dec(C1, C2, D, P):
    PT = ""
    for i in C2:
        data = (ord(i) * invmod(C1 ** D, P)) % P
        PT += chr(data)
    return PT

C1,C2 = open("./flag.ct","r").readlines()
C1 = int(C1[6:])
C2 = C2[6:]

D = 1
while dec(C1,C2,D,P)[0] != "V":
    D += 1
print(dec(C1,C2,D,P))
