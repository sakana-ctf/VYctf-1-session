flag = [118, 121, 995, 116, 102, 123, 104, 101, 492, 108, 482, 95, 65, 114, 100, 117, 493, 110, 482, 125]
line = [10, 3, 14, 4, 0, 13, 10, 3, 14, 0, 14, 0, 0, 7, 13, 5, 14, 0, 14, 7]

exp_flag = ""

for i in range(len(flag)):
    if line[i] == 14:
        data = chr(int(str(flag[i])[:2]))
    else:
        data = chr(flag[i])
    exp_flag += data

print(exp_flag)
