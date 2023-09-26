# 简单sqrt
本题由`brics-ctf2023`的`sqrt`修改而成, 主要是让大家了解sagemath数学工具(基于python).

## 程序分析
```python
# sage部分代码
from sage.all import *
import hashlib
P = Permutations(8).random_element()
print("P的平方为:",P**2)
```
第一部分由sagemath完成, 主要考点为`P ** 2`会将P的数组进行重组, 而不是直接取举证的元素平方.
```python
# python部分代码
print("加密结果为:",[x^y for x,y in zip(hashlib.sha512(str(P).encode()).digest(), open('flag.txt', 'rb').read())])
```
第二部分是简单地将矩阵使用sha512进行不可逆加密后与`flag.txt`中的二进制信息进行异或后输出为数组. 
**注意:** 在python和sage中`^`的表达含义并不相同.

## 解题思路
本题使用加密的P长度相对较短, 可以直接进行爆破:
```python
from sage.all import *
a = false
while not a:
    P = Permutations(8).random_element()
    a = bool(P ** 2 == [5, 8, 4, 3, 1, 6, 2, 7])
print(P)
print(P ** 2 == [5, 8, 4, 3, 1, 6, 2, 7])
```
得到原始P值为:
```python
[3, 7, 5, 1, 4, 6, 8, 2]
True
```
可能存在不同P由相同P**2的结果, 如果得到不同结果可以考虑重新爆破几次. 
因为异或具有可逆性, 将结果代入进python进行反解:
```python
import hashlib
P = [3, 7, 5, 1, 4, 6, 8, 2] # 爆破出的P值
N = [103, 249, 215, 167, 218, 104, 104, 230, 0, 229, 51, 131, 57, 58, 229, 121, 146, 149, 214, 108, 146, 116, 176, 92, 112, 141, 192, 208, 33, 149, 254, 138, 55, 4, 41, 167, 115, 70] #给出的加密结果
print("解密为:","".join([chr(x^y) for x,y in zip(hashlib.sha512(str(P).encode()).digest(), N)]))
```
得到flag:
```python
解密为: VYctf{We_need_4_M0re_effect1ve_Meth0d}
```
