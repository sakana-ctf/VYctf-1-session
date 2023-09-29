#include <stdio.h>
#include <stdlib.h>


void backdoor()
{
system("/bin/sh");
}

int main()
{
char buf[0x80];
printf("欢迎来到vyctf\n");
scanf("%s" , buf);
printf("bye");
return 0;
}
