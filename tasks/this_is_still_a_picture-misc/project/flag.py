from PIL import Image as img
import numpy as np
import binascii as bs

def read_pic(path):
    # 获取图像矩阵
    pic = img.open(path)
    pixel = pic.load()
    # 以rgba格式分别区分
    A = np.zeros((pic.size))
    for x in range(pic.size[0]):
        for y in range(pic.size[1]):
            A[x][y] = pixel[x,y][3] // 255
    return A

file = open("./xxd.png","w")
a_line = []
group_num = 0
pic_title = "100010010101000001001110010001110000110100001010"
xxds = []
xxd_bins = []
the_hex_num = 0
for datas in read_pic("./flag.png"):
    for data in datas:
        group_num += 1
        a_line.append(str(data)[0])
        if group_num == 8:
            the_hex_num += 1
            xxd_data = "%x"%(int("".join(a_line),2))
            if len(xxd_data) == 2:
                xxd_bin = bs.unhexlify(xxd_data).decode("utf-8","ignore")
                xxds.append(xxd_data)
            else:
                xxd_bin = bs.unhexlify("0"+xxd_data).decode("utf-8","ignore")
                xxds.append("0"+xxd_data)
            a_line = []
            group_num = 0
            xxd_bins.append(xxd_bin)
            if the_hex_num == 16:
                file.write("".join(xxds) + "  " + "".join(xxd_bins) + "\n")
                the_hex_num = 0
                xxds = []
                xxd_bins = []

file.close()
