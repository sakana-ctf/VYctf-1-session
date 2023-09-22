# 素数分解

## 原理
本题使用了rsa基本原理, 需要理解`P`, `Q`, `N`, `phin`,`E`,`D`之间的关系:
* P, Q: 素数 
* N = P * Q
* phin = (P - 1)(Q - 1): 欧拉函数, 即小于等于N的数与N互质的数量
* E: 不属于phin因子的素数
* D: E的膜反元素, 服从: (D * E) mod phin = 1
* 公钥(E, N): CT = (PT ** E)modN
* 私钥(D, N): PT = ()

## 算法
给出的`python`文件缺少`P`和`Q`, 已知`N=2771`, 属于足够小的数, 可以直接口算或者写一个简单的exp函数用循环爆破, 读取`flag.ct`文件进行ascii编码转10进制, 并按公式进行解码, 以下是个人编写的一个简单`exp.py`工具.
```python
def exp(N):
    for i in range(2,N):
        if N % i == 0:
            P = i
            Q = N // P
            return P,Q
    raise ValueError("找不到质数!")

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

# 解出P, Q
N = 2771
P,Q = exp(N)

# 简单的rsa加密技术
E = 7
N = P * Q
# N = 2771
phin = (P-1) * (Q-1)
D = invmod(E, phin)
# print(D)
# D = 1111
data = []
with open("./flag.ct","r") as file:
    for f in file.read():
        data.append(chr((ord(f) ** D) % N))
print("".join(data))
```