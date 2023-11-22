#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

char encodeLookup[] = "abz012DVop9+/ABtuvEF45678Ocdefgh3mnTUwxyPQRSCijklGHIJKLMNqrsWXYZ";
const char padCharacter = '=';

char a[] = "O9klfWU7bR44ohG1yKlJYy1SmI5yTDnScqZLNOzM6UhYMwuc4mtvxbGNuI";

void encode(const char* input, char* encoded) {
    int i = 0;
    unsigned char temp[3] = { 0 };

    int idx_enc = 0;

    size_t length = strlen(input);
    for (size_t idx = 0; idx < length; idx++) {
        temp[i++] = input[idx];
        if (i == 3) {
            encoded[idx_enc++] = encodeLookup[(temp[0] & 0xFC) >> 2];
            encoded[idx_enc++] = encodeLookup[((temp[0] & 0x03) << 4) + ((temp[1] & 0xF0) >> 4)];
            encoded[idx_enc++] = encodeLookup[((temp[1] & 0x0F) << 2) + ((temp[2] & 0xC0) >> 6)];
            encoded[idx_enc++] = encodeLookup[temp[2] & 0x3F];

            i = 0;
            temp[0] = 0; temp[1] = 0; temp[2] = 0;
        }
    }

    switch (i) {
    case 1:
        encoded[idx_enc++] = encodeLookup[(temp[0] & 0xFC) >> 2];
        encoded[idx_enc++] = encodeLookup[(temp[0] & 0x03) << 4];
        encoded[idx_enc++] = padCharacter;
        encoded[idx_enc++] = padCharacter;
        break;
    case 2:
        encoded[idx_enc++] = encodeLookup[(temp[0] & 0xFC) >> 2];
        encoded[idx_enc++] = encodeLookup[((temp[0] & 0x03) << 4) + ((temp[1] & 0xF0) >> 4)];
        encoded[idx_enc++] = encodeLookup[(temp[1] & 0x0F) << 2];
        encoded[idx_enc++] = padCharacter;
        break;
    }

    encoded[idx_enc] = '\0';
}

class init {
public:
    init() {
        strcpy(a, "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW");
    }
};

init Initializertest;

int main() {
    char str1[256]; 
    char encodedStr[512];

    printf("please input flag:");
    scanf("%255s", str1);


    size_t length = strlen(str1);
    for (size_t i = 0; i < length; i++) {
        str1[i] ^= a[i];
    }

    encode(str1, encodedStr);

    if (strcmp(encodedStr, "oENJoI1CD0Wozzqyo33mOa3sOD/wB6uIzzaZ8H/o8IUoOTwxoLOTBL8iOz4o/EoqAzAxOIUoOxoR") != 0) {
        printf("error\n");
    }
    else {
        printf("success\n");
    }

    return 0;
}
