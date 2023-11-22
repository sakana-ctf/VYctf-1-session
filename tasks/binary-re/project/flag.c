#include <stdio.h>
#include <string.h>

int shl_flag(int data) {
	int new_data = data >> 1;
	return new_data;
}

int main(void) {
	int flag[41] = {236, 242, 198, 232, 204, 246, 166, 208, 216, 190, 98, 230, 190, 154, 96, 236, 202, 190, 232, 208, 202, 190, 196, 98, 220, 104, 228, 242, 190, 232, 96, 190, 232, 208, 202, 190, 216, 202, 204, 232, 250};
	char data[41];
	printf("请输入flag:");
	scanf("%s",data);
	/*
	if (strcmp(data,flag) == 0) {
		printf("flag正确\n");
	} else {
		printf("flag错误\n");
	}
	*/
	int i;
	int new_data[41];
	for (i = 0;i < 41;i++) {
		if (data[i] - shl_flag(flag[i])) {
			printf("flag错误\n");
			return 0;
		}
	}
	printf("flag正确\n");
        return 0;
}
