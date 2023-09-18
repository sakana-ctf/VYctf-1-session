# 第一届VYctf
sakana战队的新人邀请赛, 主要面向新生举办的ctf, 出题难度偏向简单.

## 关注内容
- 出题规则:
    - 出题命名规则: 题目英文名(空格使用下划线)-题目类型
        - project: 出题文件
        - writeup: 解题过程文件
        - question: 用于存放比赛题目
- 现在还没测试过开web容器:
    - 只测试了正常下载资源提取flag
    - 之后实验ctfd里面开容器的方法
- 文件命名记得全英文, 考虑一下使用git提交的群友

## 比赛时间
* 具体时间:(暂定,等我去捞一波经费再说)
* 比赛时长:暂定1天

## 比赛题目
* pwn: (全权交给懂pwn的几位)
* re: 学会打开二进制文件已经很厉害了, 难度感觉不太容易上难度(乐)
* web: 简单的来点元素审查, post, get注入, 稍微复杂的可以试试ssti, xss, sql登录注入之类的东西 
* crypto: 口算rsa,数给小一点, elgamal解密, 试着弄弄ecc?
* misc: 图片+音频+古典密码+伪加密
* iot: 基础iot题目, 类似Arduino点灯题目

## 出题
|                              题目名称                              | 题目描述                                                                       | 题目类型 | 出题人      | 问题指向                                                                   |             flag              |
| :---------------------------------------------------------------: | :---------------------------------------------------------------------------- | :------: | :--------- | :------------------------------------------------------------------------ | :---------------------------: |
| [这亦是一种图片](./this_is_still_a_picture-misc/writeup/README.md) | 如果一个文件后缀是图片, 识别出来是图片, 并且可以以像素方式进行识别, 那它就是一张图片 |   misc   | sudopacman | 乐子题, 实际上算不上图片题, 以2进制形式打开文件, 能看到里面用0和1绘制了flag图像 | flag{5ak4na}(暂用, 后续会修改) |
|   [帕格尼尼的绝望](./paganini_is_despair-misc/writeup/README.md)   | 来一起欣赏优美的古典乐吧......等等, 为什么会有鼓点?(flag格式:vyctf{},纯小写)       |   misc   | sudopacman | 音频题, 主要涉及了midi的使用, 摩斯密码, 与少部分的ascii解密(只有两个中括号)     |       vyctf{fxxk_drum}        |






