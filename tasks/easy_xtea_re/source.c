#include <stdio.h>
#include <stdint.h>


void xteacrypt(uint32_t* v, uint32_t* k) {
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];

    int sum = 0, delta = 0x1919180;

    for (size_t i = 0; i < 32; i++)
    {
        v0 += (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + k[sum & 3]);
        sum += delta;
        v1 += (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + k[(sum >> 11) & 3]);
    }
    v[0] = v0; v[1] = v1;
}

void xteaDecrypt(uint32_t* v, uint32_t* k) {

    uint32_t v0 = v[0], v1 = v[1];
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];

    int sum = 0x1919180 * 32, delta = 0x1919180;

    for (size_t i = 0; i < 32; i++)
    {

        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + k[(sum >> 11) & 3]);
        sum -= delta;
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + k[sum & 3]);
    }
    v[0] = v0; v[1] = v1;
}


int main() {
    
    uint32_t key[4] = {0x114514,0x114514,0x114514,0x114514};

    
    printf("please input flag: \n");
    

    char inputString[24];
    scanf("%s",inputString);
    
        
    for (size_t i = 0; i < strlen(inputString) / 8; i++)
    {
        xteacrypt((uint32_t*)inputString + 2 * i, key);
    }

    int cmp[] = { 97, -112, -96, -14, -17, 72, -23, 26, -47, 96, -8, 81, 66, -52, -102, -121, 105, 99, 105, 111, 117, 115, 125 };
    
    for (size_t i = 0; i < 24; i++)
    {
        if (inputString[i] != cmp[i]) {
            printf("error");
            exit(0);
        };
    }

    printf("success");


    return 0;
}