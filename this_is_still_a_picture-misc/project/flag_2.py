import binascii as bs

file_data = open("./xxd.png")
file = open("./xxd-b.png","w")
bin_ascii = "  "
for line in file_data:
    for datas in line[11:].split(" ")[0:6]:
        try:
            data = bs.unhexlify("%x"%(int(datas,2))).decode("utf-8","ignore")
        except:
            data = bs.unhexlify("0%x"%(int(datas,2))).decode("utf-8","ignore")
        if data == "":
            bin_ascii += data
        else:
            bin_ascii += "."
    file.write(line[0:64]+bin_ascii+"\n")
    bin_ascii = "  "


