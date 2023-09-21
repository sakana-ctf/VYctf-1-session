// gcc box.c -o box -no-pie

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/prctl.h>

int install_seccomp(uint8_t *filt, unsigned short len);

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
        printf("Cannot read enough T_T\n");
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
        printf("Failed to prctl(PR_SET_NO_NEW_PRIVS) T_T\n");
         return 1;
    }
    
    printf("Good idea! flag is vyctf{test_flag}");

    return 0;
}

