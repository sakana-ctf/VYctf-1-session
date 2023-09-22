import base64,subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

def sandbox(payload): 
    if len(payload) > 0x8:
        return '这可太长了!'
    
    try:
        to_feed = base64.b64decode(payload)
    except:
        return '这可不是base64!'

    try:
        p = subprocess.Popen(['./box'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.communicate(input = to_feed, timeout=5)[0]
    except:
        return '数据提交失败了T_T'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        payload = request.form['flag']
        result = sandbox(payload)
        try:
            result = result.decode('UTF-8')
        except:
            print('让我看看有人上传了什么怪东西:',payload)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
