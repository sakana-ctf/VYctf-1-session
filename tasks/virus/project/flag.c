#include <stdio.h>

int main() {
	char flag[23] = "VYctf4";
	char fakeflag[] = "vyctf{fake_flag}";
	int data;
	int fate = 6;
	for (data = 0; data <= 15; data++){
		fate = fate + 4;
		flag[data + 6] = (fakeflag[data] ^ fakeflag[15 - data]);
		//printf("%d",data);
	}
	flag[22] = '%';
	for (data = 5; data <= 22; data++){
		fate++;
		flag[data] = flag[data] + fate;
	}

	printf("%s",flag);
	return 0;
}
