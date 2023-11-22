# 小小的也很可爱哦
简单的ElGamal加密算法, 只是对单个字符进行了简单加密, 于是可以考虑直接爆破私钥.

## 解题思路
- 加密原理:$\begin{cases} C1={E1}^R\mod{P}\\C2=(PT*{E2}^2)\mod{P} \end{cases}$
- 解密原理:$PT=[C2*({D1}^D)^{-1}]\mod{P}$

[Exp](./exp.py)使用简单的while循环可以直接爆破出结果:`VYctf{ElG4m4l_15_4n_45ymmetr1c_encrypt10n_4lg0r1thm}`