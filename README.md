# 第一届VYctf
sakana战队的新人邀请赛, 主要面向新生与刚接触网络安全的选手举办的ctf, 出题难度偏向简单.

## 比赛时间
* 第一阶段(baby, eazy, normal题型放出): 2023.10.31 8:00 - 2023.11.10 22:00
* 第二阶段(hard题型放出, 可以开始预约线下赛道): 2023.11.11 6:00 - 2023.11.21 8:00

## 成员
本次ctf由sakana战队负责:
- 致谢:
    - 感谢主办方: VY开源中国
    - 感谢本次服务器赞助: T1ng
    - 感谢本次美术提供: 陌芋Marginal
    - 感谢本次技术帮助: Zhevitz
    - 感谢本次宣发设计: sudopacman
- 本次比赛出题人:
    - sudopacman
    - nyyyddddn
    - cve_wuya
- 本次服务器运维:
    - sudopacman

## 奖品
* 前三名:授予纸质证书 + VY开源中国第一版纪念勋章 + 贴纸 + 小礼物(挂件, 本子, 明信片)四选一
* 前十名:授予电子证书

## 仓库结构
本仓库结构如下:
- player_writeup: 选手提交writeup
- scoreborad
    - borad.png: 成绩清单
    - certificate: 前十名选手证书
    - [README.md](./scoreborad/README.md): 解释
- tasks: 官方出题与writeup
- README.md: 解释文件

## 出题
|                                      题目名称                                      | 题目描述                                                                                                                                                                                                            | 题目类型 | 出题人      | 题目难度 | 问题指向                                                                     |                             flag                              |
| :-------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----: | :--------- | :-----: | :-------------------------------------------------------------------------- | :-----------------------------------------------------------: |
|   [这亦是一种图片(签到)](./tasks/this_is_still_a_picture-misc/writeup/README.md)    | 如果一个文件后缀是图片, 识别出来是图片, 并且可以以像素方式进行识别, 那它就是一张图片                                                                                                                                               |  misc   | sudopacman |  baby   | 乐子题, 实际上算不上图片题, 以2进制形式打开文件, 能看到里面用0和1绘制了flag图像   |                         vyctf{Kfc_vw50}                         |
|       [帕格尼尼的绝望](./tasks/paganini_is_despair-misc/writeup/README.md)        | 来一起欣赏优美的古典乐吧......等等, 为什么会有鼓点?<br>*格式纯小写: vyctf{xx_xx},  出题人sakana战队: sudopacman*<br>                                                                                                                  |  misc   | sudopacman |  eazy   | 音频题, 主要涉及了midi的使用, 摩斯密码, 与少部分的ascii解密(只有两个中括号)      |                        vyctf{fxxk_drum}                         |
|                 [base64逆向](./tasks/ez_base64_re/writeup.md)                 | 什么, 怎么可能知道flag<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                                                                                                                                | reverse  | nyyyddddn  |  normal  | 简单的逆向题, 添加了base64编码, 不过对于经常看base64的人来说还是很简单           |                     vyctf{W31c0m3_70_vyc7f}                      |
|               [玩具沙盒](./tasks/ez_baby_box-web/writeup/README.md)                | 你可能需要base64, 但也不一定完全需要, 尝试向网站传入点什么吧<br>*格式: vyctf{xx_xx},  出题人sakana战队: sudopacman*<br>                                                                                                               |   web   | sudopacman |  baby   | 非常有趣的web题, 主要涉及到代码审计, 还有一点小小的脑洞, 相比起来更像是闯关题     |                 vyctf{th1s_is_c0de9ate_baby_b0x}                  |
|                [素数分解](./tasks/ez_rsa-crypto/writeup/README.md)                 | 这大概是最简单的rsa加密, 解开题目甚至不需要调用任何库, 来直接口算出来吧<br>*格式: vyctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                                        |  crypto  | sudopacman |  normal  | rsa密码基础题型, 足够小的数方便在不使用工具的情况下直接得出密码                |                  vyctf{R5a_1s_M0dern_pA55w0rd}                   |
|         [简单sqrt](./tasks/Nice_to_meet_sage-crypto/writeup/README.md)          | 坏了,怎么使用不了`sage.all`呢?<br>*格式: VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                                                                         |  crypto  | sudopacman |  normal  | 主要考察对sage的使用, 在编写中sage与python存在很多语法区别, 其中还有小部分爆破    |               VYctf{We_need_4_M0re_effect1ve_Meth0d}               |
|                 [二进制](./tasks/binary-re/writeup/README.md)                 | 奇怪,为什么找不到flag在哪里呢?<br>*格式:vyctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                                                                          | reverse  | sudopacman |  normal  | ctf逆向入门题, 考察逆向工具的基本使用与gcc和汇编语言的审计能力                   |             vyctf{Shl_1s_M0ve_the_b1n4ry_t0_the_left}              |
| [大家一起和平地玩耍吧(签到)](./tasks/godot_is_the_best_engine-re/writeup/README.md) | Godot是一款神奇的引擎, 来体验一下VY开源社区在BOOOM进行开发的小游戏吧<br>[文件下载地址](https://gitee.com/cryingn/dar/releases/tag/flag)<br>*格式:VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                 | reverse  | sudopacman |  eazy   | 单纯地玩游戏, 或者进行简单地逆向, 找找关键词识别节点                         |                     VYctf{We1c0me_t0_VycTf}                      |
|                       [QAQ](./tasks/pwn_QAQ/wp_1.txt)                       | 不出意外的话pwn被扣下了, 运维背大锅<br>*格式vyctf{xx_xx},出题人sakana战队:cve_wuya*<br>                                                                                                                                          |   pwn   | cve_wuya   |  normal  |                                                                             |                     vyctf{Qaq_me4n5_s4dne5s}                     |
|               [雪(snow)](./tasks/snow-misc/writeup/writeup.md)                | 那么对于网页来说, 接下来就是大开脑洞的时间了<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                                                                                                               |  misc   | sudopacman |  normal  | 大概算检测对信息的检索能力吧, 最好还是往脑洞题出? 也不知道新生的信息检索能力怎么样 |                     vyctf{5n0w_15_834u71fu1}                     |
|        [缺少的专辑(签到)](./tasks/Missing_Albums-misc/writeup/readme.md)         | 某位不要脸的网易云音乐人将自己的专辑图片放了出来, 没记错的话好像叫陈诺?<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                          |  misc   | sudopacman |  baby   | 简单的修改图片宽高                                                            |                  VYctf{Fl4g_h1dden_Bel0w_1m4ge}                   |
|             [简单ino(签到)](./tasks/ez_ino-iot/writeup/readmd.md)              | 好奇怪, flag为什么会不对呢?<br>*格式: vyctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                                                                           |   iot   | sudopacman |  normal  | 简单的iot入门题, 考察对代码的基本审计与基础的lcd原理                            |                      vyctf{he1l0_Ardu1n0}                       |
|             [Air001](./tasks/beautiful_001-iot/writeup/README.md)              | 什么, 据说Air001专为敏感用户打造?<br>*格式:VYCTF{XX_XX},出题人sakana战队:sudopacman*<br>                                                                                                                                        |   iot   | sudopacman |  eazy   | 涉及到对PCB板工具的基本使用                                             |                      VYCTF{N1CE_T0_A1R001}                      |
|                [怎么会解不出来呢](./tasks/怎么会解不出来呢/wp.md)                | 好奇怪好奇怪, 为什么会解不出来呢?<br>**注意:** 本题涉及到部分篡改问题, 当前测试过windows defender会出现报毒情况, 玩家请谨慎下载.<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                                          | reverse  | nyyyddddn  |  hard   | 程序运行的时候在main 函数前Destination就已经被init了                           |      vyctf{Oh__y0u_v3_l34rn3d_wh4t_4n_1n1t14l1z3r_funct10n_15}       |
|             [小小的也很可爱哦](./tasks/ez_elgamal-crypto/README.md)             | 这可是最原滋原味的ElGamal加密算法哦<br>*格式: VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                                                                     |  crypto  | sudopacman |  normal  | 简单的非对称加密算法, 需要爆破私钥                                             |        VYctf{ElG4m4l_15_4n_45ymmetr1c_encrypt10n_4lg0r1thm}         |
|                  [movmovmov](./tasks/movmovmov/writeup.md)                   | movmovmovmovmovmovmov<br>*格式:vyctf{xx_xx},出题人sakana战队:nyyyddddn*<br>                                                                                                                                                  | reverse  | nyyyddddn  |  hard   | movmovmovmovmovmov                                                          |                  vyctf{M0V_MOV_M0V_MOV_M0V_MOV}                   |
|             [古老的语言(签到)](./tasks/brainfuck-crypto/writeup.md)             | sakana怕大家看不懂古老的语言, 送来了新鲜的解码工具<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                                           |  crypto  | sudopacman |  eazy   | 可以审计代码,也可以直接用vlang编译好后直接解码                                  |                     VYctf{welc0me_t0_crypt0}                     |
|        [玩蛇(签到)&玩蛇2.0](./tasks/Dont_open_f12-web/writeup/readme.md)         | Python!Python!Python!<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                                                                 |   web   | sudopacman |  eazy   | 考验绕过javascript的禁用F12策略, 或者称为一个真正的游戏大神?                    | VYctf{Pyth0n_15_thE_be5t_L4ngu4ge}<br>VYctf{Y0u_4re_the_m45ter_0f_JS} |
|             [简易曲线](./tasks/ez_curve-crypto/writeup/readme.md)              | 只取1/2了以后, 听说很多高中生能够秒解出来?<br>*VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                                                     |  crypto  | sudopacman |  hard   | 简单的几何问题, 可以通过对字符穷举爆破出来, 只不过好像不容易找参考, 难度给大一点   |   VYctf{Ge0metry_que5t1on5_4re_u5u4lly_c0mpleted_thr0ugh_ge0gebr4}    |
|          [你是什么小饼干](./tasks/we_need_admin-web/writeup/README.md)           | 我们成功修复了flask框架不会受到xss攻击的bug, 现在它可以正常被入侵了<br>*VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                                 |   web   | sudopacman |  hard   | 简单的xss攻击, 本题有较为完整的html审计, 获取cookie, 伪造cookie的渗透过程       |               VYctf{X5s_1s_0ur_f1r5t_M4ch1ne_1n_Web}               |
|        [藏匿的秘密(线下题)](./tasks/flag_is_hiding-iot/writeup/README.md)         | 本题为线下题, 线下赛道的挑战者请提前进行预约, 直到芯片全部烧毁, 每人有两小时的挑战时间<br>*VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                  |   iot   | sudopacman |  hard   | 嵌入式基础, 需要了解开发版基本原理, 能够实现烧录与测试等基本功能                |            VYctf{We_5h4ll_F1ght_0n_the_5e4s_4nd_0ce4n5}            |
|                  [osc](./tasks/osc-misc/writeup/README.md)                   | 吱吱呀呀--!这是什么奇怪的声音,请交给专业的对象处理吧<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                                          |  misc   | sudopacman |  hard   | 基本音频原理                                                                 |                        VYctf{Ch1naN4ko}                         |
|                  [easy_xtea](./tasks/easy_xtea_re/flag.txt)                  | 出题人啥都没给, 只能留个符号了 :)<br>*格式: vyctf{xx_xx}, 出题人sakana战队:nyyyddddn*<br>                                                                                                                                        | reverse  | syyyddddn  |  hard   | 逆向X密码                                                                    |                     vyctf{tea_is_delicious}                      |
|                 [kawaii病毒](./tasks/virus/writeup/README.md)                 | 作者本人保证无安全隐患, 为避免文件篡改请验证sha1sum:`4bbc59c9a4778889f463cdbf1fef397eb087afb9 virus.exe`<br>*VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                          |  virus  | sudopacman |  normal  | 基本审计能力, 或者暴力逆向?                                             |                     VYctf{SgLcLqQYZTvSlWtb}                      |
|                    [小恐龙](./tasks/color-web/README.md)                     | 我把chrome的恐龙快跑小游戏搬了过来, 为了防止大家觉得单调, 甚至多上了些颜色.<br>*格式:VYctf{xx_xx},出题人sakana战队:sudopacman*<br>                                                                                                       |   web   | sudopacman |  normal  | 十六进制隐写的玩具题                                                          |                   VYctf{fxxk_met4redctf_2023}                    |
|                [客服小祥的审判](./tasks/mygo-crypto/readme.md)                 | 你是抱着多大的觉悟说出这种话的, 你不过是一个学生, 有办法背负他人的人生吗, "什么都愿意做"就是这么沉重的话, 做不来的事就别随便说出口. 你这个人, 满脑子都只想着自己呢.<br>连接端口:`nc 47.113.145.248 32123`,*格式:VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br> |  crypto  | sudopacman |  hard   | 整活题目, 证明我们VYCTF是能实现nc题目的, 原题来自灰猫审判                     |             VYctf{k4n_b4ng_Dre4m_1t5_Myg0!!!!!_k4n_de}             |
|                        [还原大师](./tasks/readme.md)                        | 免费分享给大家的flag在传递过程中出现了信息丢失, 智慧的ctfer们能帮忙还原数据吗?<br>*格式: VYctf{xx_xx}, 出题人sakana战队:sudopacman*<br>                                                                                                  |  crypto  | sudopacman |  eazy   | 参考hackergame中的`惜字如金`, 想模拟出纠错码原理进行人工纠错                  |                  VYctf{y0u_f1xed_the_d1ct1on4ry}                  |


