datas = open("./data").readlines()
flag = [chr(int(data[2:4],16) >> 1) for data in datas]
print("".join(flag))
