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
def exp(data):
    for i in range(2,data-1):
        if data % i:
            i += 1
        else:
            return i,data//i
        i += 1
    return 0, 0

# 解出P, Q
N = 2771
P,Q = exp(N)

# 简单的rsa加密技术
E = 7
N = P * Q
# N = 2771
phin = (P-1) * (Q-1)
D = pow(E, -1, phin)
# print(D)
# D = 1111
data = []
with open("./flag.ct","r") as file:
    for f in file.read():
        data.append(chr((ord(f) ** D) % N))
print("".join(data))
```
