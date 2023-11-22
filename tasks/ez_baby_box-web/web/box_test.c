// gcc box.c -o box -no-pie

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>
#include <linux/seccomp.h>
#include <sys/prctl.h>

int install_seccomp(uint8_t *filt, unsigned short len);
void vuln();

uint32_t target = 0xdead;

int main(int argc, char **argv) {
    uint32_t filt_len;

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    read(0, &filt_len, sizeof(uint32_t));
    uint8_t *filt =  (unsigned char *)calloc(sizeof(uint8_t), filt_len);
    int res = read(0, filt, filt_len);
    if (res != filt_len) {
        printf("太多了读不完了555");
        return 1;
    }

    if (install_seccomp(filt, (unsigned short)filt_len))
        return 1;


    return 0;
}

int install_seccomp(unsigned char *filt, unsigned short filt_len) {
    struct prog {
        unsigned short len;
        unsigned char *filt;
    } rule = {
        .len = filt_len >> 3,
        .filt = filt
    };
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) < 0) {
        printf("滴滴, 安全管制!");
         return 1;
    }
    
    printf("干得漂亮! flag是vyctf{th1s_is_c0de9ate_baby_b0x}");

    return 0;
}

