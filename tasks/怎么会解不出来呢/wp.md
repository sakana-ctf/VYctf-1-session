

## 怎么会解不出来呢

这是一个先将输入数据异或上Destination然后用换表的base64encode encode输入数据，最后和oENJoI1CD0Wozzqyo33mOa3sOD/wB6uIzzaZ8H/o8IUoOTwxoLOTBL8iOz4o/EoqAzAxOIUoOxoR比较的逻辑，写脚本如果直接将异或的数据复制上去是会有问题的，动调或者查看交叉引用其实会发现，程序运行的时候在main函数前Destination就已经被init了

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4; // [esp+0h] [ebp-30Ch]
  size_t v5; // [esp+0h] [ebp-30Ch]
  size_t i; // [esp+4h] [ebp-308h]
  char Str1[512]; // [esp+8h] [ebp-304h] BYREF
  char Str[256]; // [esp+208h] [ebp-104h] BYREF

  sub_4014C0("please input flag:", v4);
  sub_401500("%255s", (char)Str);
  v5 = strlen(Str);
  for ( i = 0; i < v5; ++i )
    Str[i] ^= Destination[i];
  sub_401030(Str, (int)Str1);
  if ( !strcmp(Str1, "oENJoI1CD0Wozzqyo33mOa3sOD/wB6uIzzaZ8H/o8IUoOTwxoLOTBL8iOz4o/EoqAzAxOIUoOxoR") )
    sub_4014C0("success\n", v5);
  else
    sub_4014C0("error\n", v5);
  return 0;
}
```

在这里，所以需要异或上W才行

```c
void *__thiscall sub_401010(void *this)
{
  strcpy(Destination, "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW");
  return this;
}
```



```python
import base64

custom_base64_table = "abz012DVop9+/ABtuvEF45678Ocdefgh3mnTUwxyPQRSCijklGHIJKLMNqrsWXYZ"
custom_base64_decode_table = str.maketrans(custom_base64_table, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

flag = "oENJoI1CD0Wozzqyo33mOa3sOD/wB6uIzzaZ8H/o8IUoOTwxoLOTBL8iOz4o/EoqAzAxOIUoOxoR"

flag = base64.b64decode(flag.translate(custom_base64_decode_table)).decode('utf-8')

for i in flag:
    s = ord(i) ^ ord('W')
    print(chr(s),end="")
```

```
vyctf{Oh__y0u_v3_l34rn3d_wh4t_4n_1n1t14l1z3r_funct10n_15}
```

