flag: vyctf{W31c0m3_70_vyc7f}



```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // eax
  size_t v4; // eax
  int v5; // ecx
  char *v6; // eax
  char v8[1024]; // [esp+0h] [ebp-804h] BYREF
  char Buffer[1024]; // [esp+400h] [ebp-404h] BYREF

  sub_401010("please input flag:", v8[0]);
  v3 = _acrt_iob_func(0);
  fgets(Buffer, 1024, v3);
  v4 = strcspn(Buffer, "\n");
  if ( v4 >= 0x400 )
  {
    __report_rangecheckfailure();
    __debugbreak();
  }
  Buffer[v4] = 0;
  strlen(Buffer);
  sub_401040(v8);
  v5 = strcmp(v8, "dnljdGZ7VzMxYzBtM183MF92eWM3Zn0=");
  if ( v5 )
    v5 = v5 < 0 ? -1 : 1;
  v6 = "error\n";
  if ( !v5 )
    v6 = "success\n";
  sub_401010(v6, v8[0]);
  return 0;
}
```

分析逻辑，sub_401010("please input flag:", v8[0]); v8是输入的数据，sub_401040()函数中存在大量3 4 6相关的运算以及存在

```c
.rdata:00403160 byte_403160     db 41h                  ; DATA XREF: sub_401040+7D↑r
.rdata:00403160                                         ; sub_401040+89↑r ...
.rdata:00403161 aBcdefghijklmno db 'BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',0
```

这个索引表，很明显是base64的特征

通过在线解密解出  vyctf{W31c0m3_70_vyc7f}





