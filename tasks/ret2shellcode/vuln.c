#include <stdio.h>
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>


void init(){
  setbuf(stdin, 0LL);
  setbuf(stdout, 0LL);
  setbuf(stderr, 0LL);
}




int main() {

    init();

    // 分配的内存大小
    const size_t size = 0x1000;

    // 使用mmap分配内存
    // 参数说明：
    // 1. NULL - 让操作系统选择内存分配的地址
    // 2. size - 分配内存的大小
    // 3. PROT_READ | PROT_WRITE | PROT_EXEC - 设置内存页为可读、可写、可执行
    // 4. MAP_PRIVATE | MAP_ANONYMOUS - 内存页不与任何文件关联，且对该映射的修改不会影响其他进程
    // 5. -1 - 由于不与文件关联，因此文件描述符设置为-1
    // 6. 0 - 无文件偏移
    void *ptr = mmap(NULL, size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

    if (ptr == MAP_FAILED) {
        perror("mmap error");
        return 1;
    }


    write(1,"please input flag?\n",strlen((char *)"please input flag?\n"));

    read(0, ptr, size);


    void (*func)() = (void (*)())ptr;
    func();



    return 0;
}
