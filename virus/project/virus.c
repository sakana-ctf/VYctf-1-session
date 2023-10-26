// x86_64-w64-mingw32-gcc virus.c -o virus.exe -O0

#include <windows.h>
#include <stdio.h>

int filenum() {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile("*", &findFileData);
    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Can't find file");
        return 1;
    }

    int fileCount = 0;
    do {
        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            continue;
        }
        fileCount++;
    } while (FindNextFile(hFind, &findFileData) != 0);

    FindClose(hFind);
    return fileCount;
}

int main(){
    	char fakeflag[] = "vyctf{fake_flag}";
	char flag[23] = "VYctf{";
        int i;
	int fate = 7;
	HWND hwnd;
	hwnd=FindWindow("ConsoleWindowClass",NULL);
	if (hwnd) ShowWindow(hwnd,SW_HIDE);
	
	int num = filenum();
	char *dialogue = "hey,I'm virus.\nCan you delete a few files randomly and recommend me to other machine.\nThanks a lot~";
	for (i = 0; i <= 15; i++){
		fate = fate + 4;
                flag[i + 6] = (fakeflag[i] ^ fakeflag[15 - i]);
        }
	int data = MessageBox(0,dialogue,"Evil_virus",MB_YESNO);
	if (data == 6){
		if (num <= filenum()){
			dialogue = "I've never seen such a liar.";
		}else{
        		flag[22] = '%';
			for (i = 5; data <= 22; data++){
				fate++;
				flag[data] = flag[data] + fate;
			}
        		dialogue = flag;
		}
		
	}else{
		return 0;
	}
	data = MessageBox(0,dialogue,"Evil_virus",0);
	return 0;
}
