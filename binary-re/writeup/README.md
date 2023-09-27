# binary
  本题以[retdec](gitee.com/cryingn/retdec)工具为例进行解题. 

# 解题思路
  在linux中通过`./retdec-decompiler flag`命令对二进制文件进行反编译, 得到文件:
```bash
  flag       flag.c                flag.dsm
flag.bc     flag.config.json       flag.ll
```
  其中*flag.c*为伪代码, *flag.dsm*为汇编代码, 其他文件可参考文档, 本次writeup不进行深入解释.
  首先运行源文件:
```bash
./flag
请输入flag:test
flag错误
```
  可以大概知道文件工作逻辑是对输入信息进行判断, 如果不是flag将会输出`flag错误`.
  为方便快速理解程序, 首先阅读*flag.c* 文件, 定位到主函数(`main()`函数):
```c
// Address range: 0x117d - 0x13d0
int main(int argc, char ** argv) {
    // 0x117d
    int64_t v1; // bp-8, 0x117d
    int64_t v2 = &v1; // 0x117e
    int64_t v3 = __readfsqword(40); // 0x1189
    printf((char *)&g1);
    int64_t v4; // bp-88, 0x117d
    scanf("%s", &v4);
    int32_t v5 = 0; // 0x1392
    int64_t v6 = v5; // 0x1358
    char v7 = *(char *)(v2 - 80 + v6); // 0x135a
    uint32_t v8 = *(int32_t *)(v2 - 256 + 4 * v6); // 0x136a
    while ((int32_t)v7 == (int32_t)shl_flag((int64_t)v8)) {
        // 0x1399
        v5++;
        if (v5 >= 41) {
            // 0x13a2
            puts((char *)&g3);
            goto lab_0x13b6;
        }
        v6 = v5;
        v7 = *(char *)(v2 - 80 + v6);
        v8 = *(int32_t *)(v2 - 256 + 4 * v6);
    }
    // 0x137c
    puts((char *)&g2);
    goto lab_0x13b6;
  lab_0x13b6:;
    int64_t result = 0; // 0x13c3
    if (v3 != __readfsqword(40)) {
        // 0x13c5
        __stack_chk_fail();
        result = &g6;
    }
    // 0x13ca
    return result;
}
```
  由开头注释可知代码对应汇编语句位置在`0x117d - 0x13d0`, 其中`&g1`应该为`请输入flag`字符串, 由`scanf("%s", &v4);`可知v4为输入值, 在while循环进行判别时涉及到`shl_flag()`函数, 跳转到`shl_flag()`函数:
```c
// Address range: 0x1169 - 0x117d
int64_t shl_flag(int64_t a1) {
    // 0x1169
    return (int32_t)a1 >> 1;
}
```
  可以看到函数返还了右移1位后传递的参数(int64转化为二进制使整体右移一位), 该函数为本题的主要加密方式, 打开*flag.dsm* 文件, 定位到`0x117d - 0x13d0`处:
```nasm
0x117d:   55                                    push rbp0x117e:   48 89 e5                              mov rbp, rsp
0x1181:   53                                    push rbx0x1182:   48 81 ec 08 01 00 00                  sub rsp, 0x108
0x1189:   64 48 8b 04 25 28 00 00 00            mov rax, qword ptr fs:[0x28]
0x1192:   48 89 45 e8                           mov qword ptr [rbp - 0x18], rax
0x1196:   31 c0                                 xor eax, eax
0x1198:   c7 85 00 ff ff ff ec 00 00 00         mov dword ptr [rbp - 0x100], 0xec
0x11a2:   c7 85 04 ff ff ff f2 00 00 00         mov dword ptr [rbp - 0xfc], 0xf2
0x11ac:   c7 85 08 ff ff ff c6 00 00 00         mov dword ptr [rbp - 0xf8], 0xc6
0x11b6:   c7 85 0c ff ff ff e8 00 00 00         mov dword ptr [rbp - 0xf4], 0xe8
0x11c0:   c7 85 10 ff ff ff cc 00 00 00         mov dword ptr [rbp - 0xf0], 0xcc
0x11ca:   c7 85 14 ff ff ff f6 00 00 00         mov dword ptr [rbp - 0xec], 0xf6
0x11d4:   c7 85 18 ff ff ff a6 00 00 00         mov dword ptr [rbp - 0xe8], 0xa6
0x11de:   c7 85 1c ff ff ff d0 00 00 00         mov dword ptr [rbp - 0xe4], 0xd0
0x11e8:   c7 85 20 ff ff ff d8 00 00 00         mov dword ptr [rbp - 0xe0], 0xd8
0x11f2:   c7 85 24 ff ff ff be 00 00 00         mov dword ptr [rbp - 0xdc], 0xbe
0x11fc:   c7 85 28 ff ff ff 62 00 00 00         mov dword ptr [rbp - 0xd8], 0x62
0x1206:   c7 85 2c ff ff ff e6 00 00 00         mov dword ptr [rbp - 0xd4], 0xe6
0x1210:   c7 85 30 ff ff ff be 00 00 00         mov dword ptr [rbp - 0xd0], 0xbe
0x121a:   c7 85 34 ff ff ff 9a 00 00 00         mov dword ptr [rbp - 0xcc], 0x9a
0x1224:   c7 85 38 ff ff ff 60 00 00 00         mov dword ptr [rbp - 0xc8], 0x60
0x122e:   c7 85 3c ff ff ff ec 00 00 00         mov dword ptr [rbp - 0xc4], 0xec
0x1238:   c7 85 40 ff ff ff ca 00 00 00         mov dword ptr [rbp - 0xc0], 0xca
0x1242:   c7 85 44 ff ff ff be 00 00 00         mov dword ptr [rbp - 0xbc], 0xbe
0x124c:   c7 85 48 ff ff ff e8 00 00 00         mov dword ptr [rbp - 0xb8], 0xe8
0x1256:   c7 85 4c ff ff ff d0 00 00 00         mov dword ptr [rbp - 0xb4], 0xd0
0x1260:   c7 85 50 ff ff ff ca 00 00 00         mov dword ptr [rbp - 0xb0], 0xca
0x126a:   c7 85 54 ff ff ff be 00 00 00         mov dword ptr [rbp - 0xac], 0xbe
0x1274:   c7 85 58 ff ff ff c4 00 00 00         mov dword ptr [rbp - 0xa8], 0xc4
0x127e:   c7 85 5c ff ff ff 62 00 00 00         mov dword ptr [rbp - 0xa4], 0x62
0x1288:   c7 85 60 ff ff ff dc 00 00 00         mov dword ptr [rbp - 0xa0], 0xdc
0x1292:   c7 85 64 ff ff ff 68 00 00 00         mov dword ptr [rbp - 0x9c], 0x68
0x129c:   c7 85 68 ff ff ff e4 00 00 00         mov dword ptr [rbp - 0x98], 0xe4
0x12a6:   c7 85 6c ff ff ff f2 00 00 00         mov dword ptr [rbp - 0x94], 0xf2
0x12b0:   c7 85 70 ff ff ff be 00 00 00         mov dword ptr [rbp - 0x90], 0xbe
0x12ba:   c7 85 74 ff ff ff e8 00 00 00         mov dword ptr [rbp - 0x8c], 0xe8
0x12c4:   c7 85 78 ff ff ff 60 00 00 00         mov dword ptr [rbp - 0x88], 0x60
0x12ce:   c7 85 7c ff ff ff be 00 00 00         mov dword ptr [rbp - 0x84], 0xbe
0x12d8:   c7 45 80 e8 00 00 00                  mov dword ptr [rbp - 0x80], 0xe8
0x12df:   c7 45 84 d0 00 00 00                  mov dword ptr [rbp - 0x7c], 0xd0
0x12e6:   c7 45 88 ca 00 00 00                  mov dword ptr [rbp - 0x78], 0xca
0x12ed:   c7 45 8c be 00 00 00                  mov dword ptr [rbp - 0x74], 0xbe
0x12f4:   c7 45 90 d8 00 00 00                  mov dword ptr [rbp - 0x70], 0xd8
0x12fb:   c7 45 94 ca 00 00 00                  mov dword ptr [rbp - 0x6c], 0xca
0x1302:   c7 45 98 cc 00 00 00                  mov dword ptr [rbp - 0x68], 0xcc
0x1309:   c7 45 9c e8 00 00 00                  mov dword ptr [rbp - 0x64], 0xe8
0x1310:   c7 45 a0 fa 00 00 00                  mov dword ptr [rbp - 0x60], 0xfa
0x1317:   48 8d 05 e6 0c 00 00                  lea rax, [rip + 0xce6]
```
可以明显找到xor的[数组](./data)的十六进制形式, 写一个简单[脚本](./exp.py)即可获取flag:
```python
datas = open("./data").readlines()
flag = [chr(int(data[2:4],16) >> 1) for data in datas]
print("".join(flag))
```
得到结果:`vyctf{Shl_1s_M0ve_the_b1n4ry_t0_the_left}`