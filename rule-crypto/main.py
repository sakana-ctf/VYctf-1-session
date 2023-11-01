import base64

def function_dict(position):
    datas = [
            "1sd2jk}3l",
            "wurio456{",
            "8cvn_xm79",
            "etyufgh14",
            "sVhjlaewY",
            "fhjl_ebco",
            "Ysucinowe",
            "0nt5bw_fn"
            ]
    for data in datas:
        assert len(data) == 10,"your dictionary is not quite right."

    return datas[position[0]][position[1]]

def function_base64(left, right):
    assert left == base64.b64encode(right),"base64 verification failed."
    return left[0] & 7

def main():
    datas = []
    datas.append([function_base64(b"d2VsY29tZQ",b"welcome"),1])
    datas.append([function_base64(b"dG8",b"to"),8])
    datas.append([function_base64(b"VlljdGY",b"VYctf"),4])
    datas += [
            [7,3], [3,4], [1,9],
            [3,2], [7,0], [1,2],
            [2,5], [5,1], [0,0],
            [2,6], [3,0], [0,3],
            [5,5], [7,3], [4,2],
            [3,0], [7,7], [0,3],
            [0,0], [2,2], [7,3],
            [0,0], [1,5], [2,4],
            [1,6], [1,3], [3,2],
            [0,7]
    ]
    flag = ""
    for data in datas:
        flag += function_dict(data)
    print(flag)

main()
