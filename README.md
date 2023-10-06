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
|                                   题目名称                                   | 题目描述                                                                                                                                                                        | 题目类型 | 出题人      | 题目难度 | 问题指向                                                                     |                           flag                            |
| :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-----: | :--------- | :-----: | :-------------------------------------------------------------------------- | :-------------------------------------------------------: |
|   [这亦是一种图片(签到)](./this_is_still_a_picture-misc/writeup/README.md)    | 如果一个文件后缀是图片, 识别出来是图片, 并且可以以像素方式进行识别, 那它就是一张图片                                                                                                   |   misc   | sudopacman |   baby   | 乐子题, 实际上算不上图片题, 以2进制形式打开文件, 能看到里面用0和1绘制了flag图像   |                      vyctf{Kfc_vw50}                      |
|        [帕格尼尼的绝望](./paganini_is_despair-misc/writeup/README.md)         | 来一起欣赏优美的古典乐吧......等等, 为什么会有鼓点?<br>*格式纯小写: vyctf{xx_xx},  出题人sakana战队: sudopacman*<br>                                                                 |   misc   | sudopacman |   eazy   | 音频题, 主要涉及了midi的使用, 摩斯密码, 与少部分的ascii解密(只有两个中括号)       |                     vyctf{fxxk_drum}                      |
|                   [base64逆向](./ez_base64_re/writeup.md)                    | 什么, 怎么可能知道flag<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                                                                                    | reverse  | nyyyddddn  |  normal  | 简单的逆向题, 添加了base64编码, 不过对于经常看base64的人来说还是很简单           |                  vyctf{W31c0m3_70_vyc7f}                  |
|               [玩具沙盒](./ez_baby_box-web/writeup/README.md)                | 你可能需要base64, 但也不一定完全需要, 尝试向网站传入点什么吧<br>*格式: vyctf{xx_xx},  出题人sakana战队: sudopacman*<br>                                                              |   web    | sudopacman |   baby   | 非常有趣的web题, 主要涉及到代码审计, 还有一点小小的脑洞, 相比起来更像是闯关题      |             vyctf{th1s_is_c0de9ate_baby_b0x}              |
|                [素数分解](./ez_rsa-crypto/writeup/README.md)                 | 这大概是最简单的rsa加密, 解开题目甚至不需要调用任何库, 来直接口算出来吧<br>*格式: vyctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                       |  crypto  | sudopacman |  normal  | rsa密码基础题型, 足够小的数方便在不使用工具的情况下直接得出密码                   |               vyctf{R5a_1s_M0dern_pA55w0rd}               |
|           [简单sqrt](./Nice_to_meet_sage-crypto/writeup/README.md)           | 坏了,怎么使用不了`sage.all`呢?<br>*格式: VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                            |  crypto  | sudopacman |  normal  | 主要考察对sage的使用, 在编写中sage与python存在很多语法区别, 其中还有小部分爆破    |          VYctf{We_need_4_M0re_effect1ve_Meth0d}           |
|                   [二进制](./binary-re/writeup/README.md)                    | 奇怪,为什么找不到flag在哪里呢?<br>*格式:vyctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                             | reverse  | sudopacman |  normal  | ctf逆向入门题, 考察逆向工具的基本使用与gcc和汇编语言的审计能力                   |         vyctf{Shl_1s_M0ve_the_b1n4ry_t0_the_left}         |
| [大家一起和平地玩耍吧(签到)](./godot_is_the_best_engine-re/writeup/README.md) | Godot是一款神奇的引擎, 来体验一下VY开源社区在BOOOM进行开发的小游戏吧<br>*格式:VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                          | reverse  | sudopacman |   eazy   | 单纯地玩游戏, 或者进行简单地逆向, 找找关键词识别节点                             |                  VYctf{We1c0me_t0_VycTf}                  |
|                          [QAQ](./pwn_QAQ/wp_1.txt)                          | 不出意外的话pwn被扣下了, 运维背大锅<br>*格式vyctf{xx_xx},出题人sakana战队:cve_wuya*<br>                                                                                             |   pwn    | cve_wuya   |  normal  |                                                                             |                 vyctf{Qaq_me4n5_s4dne5s}                  |
|                 [雪(snow)](./snow-misc/writeup/writeup.md)                  | 那么对于网页来说, 接下来就是大开脑洞的时间了<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                                                                 |   misc   | sudopacman |  normal  | 大概算检测对信息的检索能力吧, 最好还是往脑洞题出? 也不知道新生的信息检索能力怎么样 |                 vyctf{5n0w_15_834u71fu1}                  |
|            [梦蝶(签到)](./Missing_Albums-misc/writeup/readme.md)             | 某位不要脸的网易云音乐人将自己的专辑图片放了出来, 没记错的话好像叫陈诺?<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                         |   misc   | sudopacman |   baby   | 简单的修改图片宽高                                                            |              VYctf{Fl4g_h1dden_Bel0w_1m4ge}               |
|               [简单ino(签到)](./ez_ino-iot/writeup/readmd.md)                | 好奇怪, flag为什么会不对呢?<br>*格式: vyctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                               |   iot    | sudopacman |  normal  | 简单的iot入门题, 考察对代码的基本审计与基础的lcd原理                            |                   vyctf{he1l0_Ardu1n0}                    |
|               [Air001](./beautiful_001-iot/writeup/README.md)               | 什么, 据说Air001专为敏感用户打造?<br>*格式:VYCTF{XX_XX},出题人sakana战队:sudopacman*<br>                                                                                           |   iot    | sudopacman |   eazy   | 涉及到对PCB板工具的基本使用                                                    |                   VYCTF{N1CE_T0_A1R001}                   |
|                  [怎么会解不出来呢](./怎么会解不出来呢/wp.md)                  | 好奇怪好奇怪, 为什么会解不出来呢?<br>**注意:** 本题涉及到部分篡改问题, 当前测试过windows defender会出现报毒情况, 玩家请谨慎下载.<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br> | reverse  | nyyyddddn  |   hard   | 程序运行的时候在main 函数前Destination就已经被init了                           | vyctf{Oh__y0u_v3_l34rn3d_wh4t_4n_1n1t14l1z3r_funct10n_15} |
|               [小小的也很可爱哦](./ez_elgamal-crypto/README.md)               | 这可是最原滋原味的ElGamal加密算法哦<br>*格式: VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                       |  crypto  | sudopacman |  normal  | 简单的非对称加密算法, 需要爆破私钥                                             |   VYctf{ElG4m4l_15_4n_45ymmetr1c_encrypt10n_4lg0r1thm}    |
|                     [movmovmov](./movmovmov/writeup.md)                     | movmovmovmovmovmovmov<br>*格式:vyctf{xx_xx},出题人sakana战队:nyyyddddn*<br>                                                                                                      | reverse  | nyyyddddn  |   hard   | movmovmovmovmovmov                                                          |              vyctf{M0V_MOV_M0V_MOV_M0V_MOV}               |
|               [古老的语言(签到)](./brainfuck-crypto/writeup.md)               | sakana怕大家看不懂古老的语言, 送来了新鲜的解码工具<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                            |  crypto  | sudopacman |   eazy   | 可以审计代码,也可以直接用vlang编译好后直接解码                                  |                 VYctf{welc0me_t0_crypt0}                  |
|             [玩蛇(签到)](./Dont_open_f12-web/writeup/readme.md)              | Python!Python!Python!<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                     |   web    | sudopacman |   eazy   | 考验绕过javascript的禁用F12策略, 或者称为一个真正的游戏大神?                    |            VYctf{Pyth0n_15_thE_be5t_L4ngu4ge}             |


