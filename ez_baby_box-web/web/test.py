import base64,subprocess

print_data = bytes("",encoding="utf-8")
data = base64.b64encode(print_data)

def sandbox(payload): 
    if type(payload) != bytes:
        return '这不是二进制哦T_T'

    if len(payload) > 0x400:
        return '太长了T_T'
    
    try:
        to_feed = base64.b64decode(payload)
    except:
        return '这不是base64编码哟T_T'

    try:
        p = subprocess.Popen(['./box'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("box_test测试值:",p.communicate(input = to_feed, timeout=5)[0])
    except:
        return '数据提交失败了T_T'

print(sandbox(data))
