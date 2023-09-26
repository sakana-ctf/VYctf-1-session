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
|                                 题目名称                                 | 题目描述                                                                                                               | 题目类型 | 出题人      | 题目难度 | 问题指向                                                                   |                  flag                  |
| :---------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------- | :-----: | :--------- | :-----: | :------------------------------------------------------------------------ | :------------------------------------: |
| [这亦是一种图片(签到)](./this_is_still_a_picture-misc/writeup/README.md) | 如果一个文件后缀是图片, 识别出来是图片, 并且可以以像素方式进行识别, 那它就是一张图片                                         |   misc   | sudopacman |   baby   | 乐子题, 实际上算不上图片题, 以2进制形式打开文件, 能看到里面用0和1绘制了flag图像 |            vyctf{Kfc_vw50}             |
|      [帕格尼尼的绝望](./paganini_is_despair-misc/writeup/README.md)      | 来一起欣赏优美的古典乐吧......等等, 为什么会有鼓点?<br>*格式纯小写: vyctf{xx_xx},  出题人sakana战队: sudopacman*<br>        |   misc   | sudopacman |   eazy   | 音频题, 主要涉及了midi的使用, 摩斯密码, 与少部分的ascii解密(只有两个中括号)     |            vyctf{fxxk_drum}            |
|                 [base64逆向](./ez_base64_re/writeup.md)                 | 什么, 怎么可能知道flag<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                           | reverse  | nyyyddddn  |  normal  | 简单的逆向题, 添加了base64编码, 不过对于经常看base64的人来说还是很简单         |        vyctf{W31c0m3_70_vyc7f}         |
|             [玩具沙盒](./ez_baby_box-web/writeup/README.md)              | 你可能需要base64, 但也不一定完全需要, 尝试向网站传入点什么吧<br>*格式: vyctf{xx_xx},  出题人sakana战队: sudopacman*<br>     |   web    | sudopacman |   baby   | 非常有趣的web题, 主要涉及到代码审计, 还有一点小小的脑洞, 相比起来更像是闯关题    |    vyctf{th1s_is_c0de9ate_baby_b0x}    |
|              [素数分解](./ez_rsa-crypto/writeup/README.md)               | 这大概是最简单的rsa加密, 解开题目甚至不需要调用任何库, 来直接口算出来吧<br>*格式: vyctf{xx_xx}, 出题人sakana战队:sudopacman* |  crypto  | sudopacman |  normal  | rsa密码基础题型, 足够小的数方便在不使用工具的情况下直接得出密码                 |     vyctf{R5a_1s_M0dern_pA55w0rd}      |
|        [简单sqrt](./Nice_to_meet_sage-crypto/writeup/README.md)         | 坏了,怎么使用不了`sage.all`呢?<br>*格式: VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                  |  crypto  | sudopacman |  normal  | 主要考察对sage的使用, 在编写中sage与python存在很多语法区别, 其中还有小部分爆破  | VYctf{We_need_4_M0re_effect1ve_Meth0d} |

