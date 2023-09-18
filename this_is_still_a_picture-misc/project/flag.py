import numpy as np
import binascii as bs
import re
import random as rd

a = open("flag.ascll").readlines()
b = open("bin.xxd").readlines()
flag_test = open("flag.test","a")

null = b'\x00'.decode()
matrix = np.zeros((10,84))
random_data = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def get_pad(matrix,pad_num):
    # 将数据用0进行填充
    matrix = np.pad(matrix,((0,0),
                  (pad_num,pad_num)),
                  mode = 'constant',
                  constant_values = (0,0)
                  )
    len_x = len(matrix[0])
    np_zeros = np.zeros((pad_num,len_x))
    matrix = np.vstack((np_zeros,matrix,np_zeros))
    return matrix

def get_data(lines):
    the_data = re.findall(r".{2}",lines)
    data = ""
    for i in the_data:
        u = bs.unhexlify(i).decode("utf-8","ignore")
        if u != null:
            data += u
        else:
            data += "."
    return data

for lines in range(len(a)):
    for word in range(len(a[lines])):
        if a[lines][word] == "#":
            matrix[lines][word] = 1

matrix = get_pad(matrix.T,11)

for y in range(len(matrix)):
    lines = "00000000000000000000000000000000"
    lines = list(lines)
    for x in range(len(matrix[y])):
        if matrix[y][x] == 1:
            lines[x] = random_data[rd.randint(0,14)]
    lines = "".join(lines)
    #print(b[y][0:9]," ",lines[0:4]," ",lines[4:8]," ",lines[8:12]," ",lines[12:16]," ",lines[16:20]," ",lines[20:24]," ",lines[24:28]," ",lines[28:32],"  ",get_data(lines))
    data = b[y][0:9]+" "+str(lines[0:4])+" "+str(lines[4:8])+" "+str(lines[8:12])+" "+str(lines[12:16])+" "+str(lines[16:20])+" "+str(lines[20:24])+" "+str(lines[24:28])+" "+str(lines[28:32])+"  "+str(get_data(lines))+"\n"
    flag_test.write(data)









