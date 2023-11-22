# 玩具沙盒
本题参考自codegate2023(韩赛预赛)的杂项题目: baby_sandbox, 本次出题对题目进行了简化, 只需要了解网站的post方法与进行简单审计便可以完成题目.

## 解题思路
### 审计代码
对文件进行审计, 遇到`box.c`不用害怕, 我们从标志着**main**的`main.py`文件入手:
```python
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
```
以上代码可以简单判断出是这次的沙盒部分, 主要进行三次判别: payload长度, base64编码, 调用box文件. 先不急着考虑绕过问题, 继续看以下代码:
```python
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
```
明显为flask网站框架的代码, 上面提供了两种方式: get与post, 其中如果识别对`flag`进行`POST`方法的提交会返还`result.html`文件, 否则返还`index.html`文件, 本次题目我们需要获得的应该是`result.html`文件.
再看`box.c`部分代码:
```c
int main(int argc, char **argv) {
    uint32_t filt_len;

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    read(0, &filt_len, sizeof(uint32_t));
    uint8_t *filt =  (unsigned char *)calloc(sizeof(uint8_t), filt_len);
    int res = read(0, filt, filt_len);
    if (res != filt_len) {
        printf("太多了读不完了555");
        return 1;
    }

    if (install_seccomp(filt, (unsigned short)filt_len))
        return 1;


    return 0;
}
```
以上代码主要用于读取输入的数据，对数据进行过滤, setvbuf()函数用于设置缓冲区, 然后读取文件, 对数据长度进行判别.
```c
int install_seccomp(unsigned char *filt, unsigned short filt_len) {
    struct prog {
        unsigned short len;
        unsigned char *filt;
    } rule = {
        .len = filt_len >> 3,
        .filt = filt
    };
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) < 0) {
        printf("滴滴, 安全管制!");
         return 1;
    }
    
    printf("干得漂亮! flag是vyctf{test_flag}");

    return 0;
}

```
后半段代码只做了简单的权限管制, 用于禁用新的权限分配, 如果符合条件便能够输出flag. 
### 实战
首先是工具的使用, 这里提供两种方法:
* **hackbar**
   作为老牌渗透工具, 确实能帮大家解决很多简单的事, 比如`post`, 不同于`get`方法, `post`无法直接在网站中使用, **hackbar**提供了很方便的`post`方法, 在浏览器插件官网找到**hackbar**安装好后可通过`f12`找到工具进行`post`传参;
* **python**
   **python**作为当今简单的主流编程语言, 能做到很多甚至个人想象不到的事, 使用**python**进行`post`传参需要了解一定的**python**方面知识, 我将脚本提交到了下面以供大家学习交流;
* **curl**
   **curl**是linux中自带的一个强大的网络工具, 通过`-d`(或者`--data`)可以直接进行`post`传参.

获取传参方式后可对给出方法进行实验, 由python部分代码可知传入参数需要足够短而且为base64格式, 在c语言中会对信息进行重新检查, 并在权限问题进行阻断, 有个很简单的方法: 在base64编码中无输出依旧属于base64编码, 所以可以直接传入空白参数, 拿到flag.<br>

### 脚本
```python
#!/bin/python
import urllib.request
url = "http://127.0.0.1:8000"
datas = "flag= ".encode()
#data = f'name=%7b%25{code}%25%7d&team_name'.encode()
def post(url,data):
    html = urllib.request.urlopen(url,data=data)
    html = html.read()
    html = html.decode()
    return html

if __name__ == "__main__":
    print(post(url,datas))
```