import base64,subprocess
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

def sandbox(payload): 
    if len(payload) > 0x8:
        return '这可太长了!'
    
    try:
        to_feed = base64.b64decode(payload)
    except:
        return '这可不是base64!'
    print(to_feed)
    try:
        p = subprocess.Popen(['./box'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.communicate(input = to_feed, timeout=5)[0]
    except:
        return '数据提交失败了T_T'

@app.route('/baby_box', methods=["GET", "POST"])
def index():
    index_data = "<h1>前端呢?前端救一救啊QAQ...</h1>"
    result_data = "<h1>{result}</h1>"
    if request.method == "POST":
        payload = request.form['flag']
        result = sandbox(payload)
        try:
            result = result.decode('UTF-8')
        except:
            print('让我看看有人上传了什么怪东西:',payload)
        return result_data.format(result = result)
    return index_data

@app.route("/python")
def main():
    html = r"""<!DOCTYPE html>
        <html>
        <head>
                <title>python!!!</title>
                <meta charset="UTF-8">
                <meta name="game" content="贪吃蛇">
                <meta name="message" content="where is my flag">
                <style type="text/css">
                *{margin:0;}
                .map{
                    margin:100px auto;
                    height:600px;
                    width:900px;
                    background:#d4f0fc;
                    border:10px solid #3c3c3c80;
                    border-radius:4px;
                }
                </style>
        </head>
        
        <body>
        <div class="map">
        <canvas id="canvas" height="600" width="900">
        
        </canvas>
        </div>
        
        <script type="text/javascript">
         //获取绘制工具
                /*
                var canvas = document.getElementById("canvas");
                var ctx = canvas.getContext("2d");//获取上下文
                ctx.moveTo(0,0);
                ctx.lineTo(450,450);*/
                var c=document.getElementById("canvas");
            var ctx=c.getContext("2d");
            /*ctx.beginPath();
            ctx.moveTo(0,0);
            ctx.lineTo(450,450);
            ctx.stroke();
            */
            var time_data = 130; //刷新速度
            var snake =[];//定义一条蛇，画蛇的身体
            var snakeCount = 6;//初始化蛇的长度
                var foodx =0;
                var foody =0;
            var togo =0;
            function drawtable()//画地图的函数
            {
                for(var i=0;i<60;i++)//画竖线
                {
                        ctx.strokeStyle="black";
                        ctx.beginPath();
                        ctx.moveTo(15*i,0);
                        ctx.lineTo(15*i,600);
                        ctx.closePath();
                        ctx.stroke();
                }
                for(var j=0;j<40;j++)//画横线
                {
                        ctx.strokeStyle="black";
                        ctx.beginPath();
                        ctx.moveTo(0,15*j);
                        ctx.lineTo(900,15*j);
                        ctx.closePath();
                        ctx.stroke();
                }
        
                for(var k=0;k<snakeCount;k++)//画蛇的身体
                                {
                                ctx.fillStyle="#336f26a6";
                                if (k==snakeCount-1)
                                {
                                        ctx.fillStyle="#8a3a3a";//蛇头的颜色与身体区分开
                                }
                                ctx.fillRect(snake[k].x,snake[k].y,15,15);//前两个数是矩形的起始坐标，后两个 数是矩形的长宽。
        
                                }
                                //绘制食物
                        ctx.fillStyle ="#c41414";
                     ctx.fillRect(foodx,foody,15,15);
                     ctx.fill();
        
            }
        
        
            function start()//定义蛇的坐标
            {
                //var snake =[];//定义一条蛇，画蛇的身体
                //var snakeCount = 6;//初始化蛇的长度
        
                        for(var k=0;k<snakeCount;k++)
                        {
                                snake[k]={x:k*15,y:0};
        
                    }
        
                          drawtable();
                  addfood();//在start中调用添加食物函数
        
            }
        
            function addfood()
                {
                foodx = Math.floor(Math.random()*60)*15; //随机产生一个0-1之间的数
                foody = Math.floor(Math.random()*40)*15;
        
                        for (var k=0;k<snake;k++)
                        {
                                if (foodx==snake[k].x&&foody==sanke[k].y)//防止产生的随机食物落在蛇身上
                                {
                                addfood();
                                }
                        }
        
        
                }
        
           function move()
           {
                switch (togo)
                {
                case 1: snake.push({x:snake[snakeCount-1].x-15,y:snake[snakeCount-1].y}); break;
                case 2: snake.push({x:snake[snakeCount-1].x,y:snake[snakeCount-1].y-15}); break;
                case 3: snake.push({x:snake[snakeCount-1].x+15,y:snake[snakeCount-1].y}); break;
                case 4: snake.push({x:snake[snakeCount-1].x,y:snake[snakeCount-1].y+15}); break;
                case 5: snake.push({x:snake[snakeCount-1].x-15,y:snake[snakeCount-1].y-15}); break;
                case 6: snake.push({x:snake[snakeCount-1].x+15,y:snake[snakeCount-1].y+15}); break;
                default: snake.push({x:snake[snakeCount-1].x+15,y:snake[snakeCount-1].y});
                }
            snake.shift();//删除数组第一个元素
                ctx.clearRect(0,0,900,600);//清除画布重新绘制
                isEat();
                isDead();
                drawtable();
           }
        
           function keydown(e)
           {
           switch(e.keyCode)
                        {
                         case 37: togo=1; break;
                         case 38: togo=2; break;
                         case 39: togo=3; break;
                         case 40: togo=4; break;
                         case 65: togo=5; break;
                         case 68: togo=6; break;
                        }
           }
        
           function isEat()//吃到食物后长度加1
           {
            if(snake[snakeCount-1].x==foodx&&snake[snakeCount-1].y==foody)
           {
                        addfood();
                        snakeCount++;
                        time_data = time_data - 2;
                        snake.unshift({x:-15,y:-15});
                        if(snakeCount==60){
                            alert('恭喜你拿到了flag: VYctf{Pyth0n_15_thE_be5t_L4ngu4ge}')
                        }
           }
        
           }
        
           function isDead()
           {
            if (snake[snakeCount-1].x>885||snake[snakeCount-1].y>585||snake[snakeCount-1].x<0||snake[snakeCount-1].y<0)
                        {
                        alert("不会有人还没通关吧, 杂鱼杂鱼❤");
                        window.location.reload();
                        }
           }
        
            document.onkeydown=function(e)
        {
                keydown(e);
        
        }
        window.onload = function()//调用函数
        {
                start();
                setInterval(move,time_data);
                drawtable();
        }
        //禁用右键（防止右键查看源代码） 
        window.oncontextmenu = function () { return false; }
        //禁止任何键盘敲击事件（防止F12和shift+ctrl+i调起开发者工具） 
        window.onkeydown = window.onkeyup = window.onkeypress = function () {
                window.event.returnValue = false;
                return false;
                }
                //如果用户在工具栏调起开发者工具，那么判断浏览器的可视高度和可视宽度是否有改变，如有改变则关闭本页面 
        var h = window.innerHeight, w = window.innerWidth;
        window.onresize = function () {
                if (h != window.innerHeight || w != window.innerWidth) {
                        window.close();
                        window.location = "about:blank";
                }
        }
        </script>
        </body>
        </html>   
        
    """
    return html

@app.route("/dinosaur")
def dinosaur():
    html = r"""<!doctype html>
    <html>
    
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
        <title>chrome小恐龙dino</title>
        <style>
            body,
            html {
                padding: 0;
                margin: 0;
                width: 100%;
                height: 100%
            }
    
            .icon {
                -webkit-user-select: none;
                user-select: none;
                display: inline-block
            }
    
            .icon-offline {
                content: -webkit-image-set(url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABIAQMAAABvIyEEAAAABlBMVEUAAABTU1OoaSf/AAAAAXRSTlMAQObYZgAAAGxJREFUeF7tyMEJwkAQRuFf5ipMKxYQiJ3Z2nSwrWwBA0+DQZcdxEOueaePp9+dQZFB7GpUcURSVU66yVNFj6LFICatThZB6r/ko/pbRpUgilY0Cbw5sNmb9txGXUKyuH7eV25x39DtJXUNPQGJtWFV+BT/QAAAAABJRU5ErkJggg==") 1x, url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJAAAACQBAMAAAAVaP+LAAAAGFBMVEUAAABTU1NNTU1TU1NPT09SUlJSUlJTU1O8B7DEAAAAB3RSTlMAoArVKvVgBuEdKgAAAJ1JREFUeF7t1TEOwyAMQNG0Q6/UE+RMXD9d/tC6womIFSL9P+MnAYOXeTIzMzMzMzMzaz8J9Ri6HoITmuHXhISE8nEh9yxDh55aCEUoTGbbQwjqHwIkRAEiIaG0+0AA9VBMaE89Rogeoww936MQrWdBr4GN/z0IAdQ6nQ/FIpRXDwHcA+JIJcQowQAlFUA0MfQpXLlVQfkzR4igS6ENjknm/wiaGhsAAAAASUVORK5CYII=") 2x);
                position: relative
            }
    
            .hidden {
                display: none
            }
    
            .offline .interstitial-wrapper {
                color: #2b2b2b;
                font-size: 1em;
                line-height: 1.55;
                margin: 0 auto;
                max-width: 600px;
                padding-top: 100px;
                width: 100%
            }
    
            .offline .runner-container {
                height: 150px;
                max-width: 600px;
                overflow: hidden;
                position: absolute;
                top: 35px;
                width: 44px
            }
    
            .offline .runner-canvas {
                height: 150px;
                max-width: 600px;
                opacity: 1;
                overflow: hidden;
                position: absolute;
                top: 0;
                z-index: 2
            }
    
            .offline .controller {
                background: rgba(247, 247, 247, .1);
                height: 100vh;
                left: 0;
                position: absolute;
                top: 0;
                width: 100vw;
                z-index: 1
            }
    
            #offline-resources {
                display: none
            }
    
            @media (max-width:420px) {
    
                .suggested-left>#control-buttons,
                .suggested-right>#control-buttons {
                    float: none
                }
    
                .snackbar {
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    border-radius: 0
                }
            }
    
            @media (max-height:350px) {
                h1 {
                    margin: 0 0 15px
                }
    
                .icon-offline {
                    margin: 0 0 10px
                }
    
                .interstitial-wrapper {
                    margin-top: 5%
                }
    
                .nav-wrapper {
                    margin-top: 30px
                }
            }
    
            @media (min-width:600px) and (max-width:736px) and (orientation:landscape) {
                .offline .interstitial-wrapper {
                    margin-left: 0;
                    margin-right: 0
                }
            }
    
            @media (min-width:420px) and (max-width:736px) and (min-height:240px) and (max-height:420px) and (orientation:landscape) {
                .interstitial-wrapper {
                    margin-bottom: 100px
                }
            }
    
            @media (min-height:240px) and (orientation:landscape) {
                .offline .interstitial-wrapper {
                    margin-bottom: 90px
                }
    
                .icon-offline {
                    margin-bottom: 20px
                }
            }
    
            @media (max-height:320px) and (orientation:landscape) {
                .icon-offline {
                    margin-bottom: 0
                }
    
                .offline .runner-container {
                    top: 10px
                }
            }
    
            @media (max-width:240px) {
                .interstitial-wrapper {
                    overflow: inherit;
                    padding: 0 8px
                }
            }
            .flag {
                background-color: rgb(255, 242, 226);
                height: 30px;
                width: 100%;
                display: flex;
            }
            li {
                width: 7.8px;
            }
        </style>
        <script>eval(function (i, a, e, o, t, c) { if (t = function (i) { return (i < 62 ? "" : t(parseInt(i / 62))) + (35 < (i %= 62) ? String.fromCharCode(i + 29) : i.toString(36)) }, !"".replace(/^/, String)) { for (; e--;)c[t(e)] = o[e] || t(e); o = [function (i) { return c[i] }], t = function () { return "\\w+" }, e = 1 } for (; e--;)o[e] && (i = i.replace(new RegExp("\\b" + t(e) + "\\b", "g"), o[e])); return i }('(j(){j c(a,b){W(c.43)U c.43;c.43=i;i.1T=N.37(a);i.8x=i.V=1v;i.6k=i.1T.37("#7J-42");i.o=b||c.o;i.s=c.4e;i.1B=i.J=i.D=i.K=1v;i.2i=i.1Y=i.2v=i.1M=0;i.1j=1A/60;i.1u=i.o.3A;i.1d=[];i.2H=i.2J=i.1c=i.1k=i.2z=!1;i.1O=0;i.2D=1v;i.4q=0;i.7h=1v;i.2f={};i.2L=1v;i.7g={};i.6R=0;i.6c()?i.6g():i.6z()}j p(a,b){U P.2F(P.2G()*(b-a+1))+a}j A(a){C b=a.X/4*3;a=6C(a);C c=G 6E(b);c=G 6G(c);Y(C g=0;g<b;g++)c[g]=a.78(g);U c.61}j q(){U w?(G 79).7i():7j.7k()}j u(a,b,c,g){i.K=a;i.D=a.1z("2d");i.2j=g;i.4l=b;i.4d=c;i.R()}j y(a,b){U G h(a.x+b.x,a.y+b.y,a.F,a.T)}j z(a,b){C c=!1,g=b.x;a.x<g+b.F&&a.x+a.F>g&&a.y<b.y+b.T&&a.T+a.y>b.y&&(c=!0);U c}j h(a,b,c,g){i.x=a;i.y=b;i.F=c;i.T=g}j n(a,b,c,g,e,d,h){i.D=a;i.O=c;i.S=b;i.3s=e;i.1r=p(1,n.41);i.s=g;i.1F=!1;i.E=g.B+(h||0);i.F=i.I=0;i.19=[];i.1K=i.1b=i.1I=i.3Y=0;i.1f(d)}j e(a,b){i.K=a;i.D=a.1z("2d");i.O=b;i.1b=i.2e=i.I=i.E=0;i.2r=[];i.1K=i.3q=i.3U=i.3T=0;i.1j=1A/60;i.o=e.o;i.Q=e.Q.1V;i.1w=i.1H=!1;i.1E=0;i.1t=i.3n=!1;i.7P=i.3m=0;i.1f()}j k(a,b,f){i.K=a;i.D=a.1z("2d");i.4L=c.1a;i.O=b;i.x=0;i.y=5;i.3i=i.2a=i.87=0;i.64=1v;i.2N=[];i.2h=!1;i.2O="";i.3g=i.1Z=0;i.3f=!1;i.o=k.o;i.1G=i.o.4c;i.1f(f)}j l(a,b,c){i.K=a;i.D=i.K.1z("2d");i.O=b;i.E=i.39=c;i.I=0;i.1F=!1;i.4Z=p(l.o.6t,l.o.63);i.1f()}j d(a,b,c){i.O=b;i.K=a;i.D=a.1z("2d");i.E=c-50;i.I=30;i.1l=i.1L=0;i.39=c;i.1s=[];i.2Z=!1;i.4j()}j m(a,b){i.O=b;i.K=a;i.D=a.1z("2d");i.1S={};i.s=m.s;i.2V=[i.O.x,i.O.x+i.s.B];i.E=[];i.I=0;i.52=.5;i.5V();i.R()}j v(a,b,c,g){i.K=a;i.D=i.K.1z("2d");i.o=v.o;i.s=c;i.3s=g;i.1d=[];i.2k=[];i.8M=[0,0];i.5s=i.o.3L;i.O=b;i.3l=1v;i.23=[];i.5q=i.o.4A;i.2P=1v;i.1f()}1h.5o=c;C r=1<1h.6s,w=/8Y|8V|8U/.5l(1h.2R.8S),t=/8R/.5l(1h.2R.8Q)||w;c.o={5C:.8N,4A:.2,5O:10,5W:8L,3L:.5,4J:8H,51:.6,2U:.6,5a:12,5c:8F,5g:8E,5j:3,4i:6,41:3,4k:2,5p:13,2W:35,5v:1.2,5x:"8D-45",3A:6,2X:3};c.4e={B:2Y,L:5Q};c.1i={4B:"5Y-K",5Z:"5Y-64",1D:"1c",6l:"4C-2b",4H:"2H",4K:"4M",4N:"4M-8B",4T:"8A"};c.1W={33:{3N:{x:8z,y:2},3O:{x:8y,y:2},3P:{x:86,y:2},3S:{x:2,y:54},3W:{x:8v,y:2},3Z:{x:8u,y:2},2w:{x:2,y:2},3a:{x:8t,y:2},4a:{x:8q,y:2},28:{x:8p,y:2}},3b:{3N:{x:8o,y:2},3O:{x:8m,y:2},3P:{x:8l,y:2},3S:{x:2,y:8k},3W:{x:8j,y:2},3Z:{x:8i,y:2},2w:{x:2,y:2},3a:{x:8h,y:2},4a:{x:8f,y:2},28:{x:8e,y:2}}};c.4t={4v:"2b-4x-8c",5R:"2b-4x-8a",5U:"2b-4x-89"};c.1P={2q:{38:1,32:1},4F:{40:1},2w:{13:1}};c.M={6i:"7Z",7Y:"7W",2K:"7V",3k:"7U",2I:"7T",2C:"7S",4O:"4P",2E:"7N",1J:"7M",4U:"7K",4V:"4W",4X:"7I",4Y:"7H"};c.1y={6c:j(){U!1},6g:j(){i.V=N.2t("3V");i.V.3p=c.1i.4K;i.V.7G=7F.7E("7C");i.1T.2s(i.V);N.Z(c.M.2K,j(a){c.1P.2q[a.3r]&&(i.V.2A.5f(c.1i.4N),N.37(".4C").2A.5f("4C-7B"))}.1q(i))},7A:j(a,b){W(a 48 i.o&&7z 0!=b)5k(i.o[a]=b,a){1n"2U":1n"2W":1n"2X":i.J.o[a]=b;3t;1n"5a":i.J.5n(b);3t;1n"3A":i.3u(b)}},6z:j(){r?(c.1a=N.3v("2b-45-2x"),i.26=c.1W.3b):(c.1a=N.3v("2b-45-1x"),i.26=c.1W.33);c.1a.7y?i.1f():c.1a.Z(c.M.4Y,i.1f.1q(i))},5t:j(){W(!w){i.2L=G 7x;C a=N.3v(i.o.5x).7v,b;Y(b 48 c.4t){C f=a.3v(c.4t[b]).7u;f=f.3y(f.7t(",")+1);f=A(f);i.2L.7s(f,j(a,b){i.2f[a]=b}.1q(i,b))}}},3u:j(a){C b=a||i.1u;2Y>i.s.B?(a=b*i.s.B/2Y*i.o.5v,i.1u=a>b?b:a):a&&(i.1u=a)},1f:j(){N.37("."+c.1i.6l).1m.7r="5B";i.4m();i.3u();i.V=N.2t("3V");i.V.3p=c.1i.5Z;C a=i.V,b=i.s.B,f=i.s.L,g=c.1i.7q,d=N.2t("K");d.3p=g?c.1i.4B+" "+g:c.1i.4B;d.F=b;d.T=f;a.2s(d);i.K=d;i.D=i.K.1z("2d");i.D.7p="#7o";i.D.7l();c.4p(i.K);i.2l=G v(i.K,i.26,i.s,i.o.51);i.1B=G k(i.K,i.26.3a,i.s.B);i.J=G e(i.K,i.26.4a);i.1T.2s(i.V);t&&i.5J();i.5K();i.H();1h.Z(c.M.4O,i.5M.1q(i))},5J:j(){i.1X=N.2t("3V");i.1X.3p=c.1i.4T;i.1T.2s(i.1X)},5M:j(){i.2D||(i.2D=7f(i.4m.1q(i),5P))},4m:j(){7e(i.2D);i.2D=1v;C a=1h.7d(i.1T);a=7c(a.5T.3y(0,a.5T.X-2));i.s.B=i.1T.7a-2*a;i.K&&(i.K.F=i.s.B,i.K.T=i.s.L,c.4p(i.K),i.1B.4w(i.s.B),i.3E(),i.2l.H(0,0,!0),i.J.H(0),i.1k||i.1c||i.2J?(i.V.1m.F=i.s.B+"1C",i.V.1m.T=i.s.L+"1C",i.1B.H(0,P.2m(i.1M)),i.3F()):i.J.R(0,0),i.1c&&i.2n&&(i.2n.62(i.s.B),i.2n.R()))},4I:j(){W(i.2z||i.1c)i.1c&&i.3G();3H{i.1U=!0;i.J.1U=!0;C a="@-74-73 69 { 6S { F:"+e.o.B+"1C }6P { F: "+i.s.B+"1C }}",b=N.2t("1m");b.6N=a;N.6M.2s(b);i.V.Z(c.M.6i,i.6e.1q(i));i.V.1m.6f="69 .4s 6L-6K 1 6J";i.V.1m.F=i.s.B+"1C";i.2z=i.1k=!0}},6e:j(){i.2i=0;i.1U=!1;i.J.1U=!1;i.V.1m.6f="";i.4q++;N.Z(c.M.4U,i.3I.1q(i));1h.Z(c.M.4V,i.3I.1q(i));1h.Z(c.M.4X,i.3I.1q(i))},3E:j(){i.D.6H(0,0,i.s.B,i.s.L)},H:j(){i.4G=!1;C a=q(),b=a-(i.1Y||a);i.1Y=a;W(i.1k){i.3E();i.J.1H&&i.J.6n(b);i.2i+=b;a=i.2i>i.o.5W;1!=i.J.3m||i.1U||i.4I();i.1U?i.2l.H(0,i.1u,a):(b=i.2z?b:0,i.2l.H(b,i.1u,a,i.2H));W(a)a:{C f=i.2l.1d[0],g=i.J;a=G h(g.E+1,g.I+1,g.o.B-2,g.o.L-2);C d=G h(f.E+1,f.I+1,f.S.F*f.1r-2,f.S.T-2);W(z(a,d)){f=f.19;g=g.1w?e.19.1Q:e.19.1N;Y(C k=0;k<g.X;k++)Y(C x=0;x<f.X;x++){C l=y(g[k],a),m=y(f[x],d);W(z(l,m)){a=[l,m];3t a}}}a=!1}a?i.6q():(i.1M+=i.1u*b/i.1j,i.1u<i.o.5p&&(i.1u+=i.o.5C));i.1B.H(b,P.2m(i.1M))&&i.2u(i.2f.5U);i.1O>i.o.5c?(i.1O=0,i.3f=!1,i.3K()):i.1O?i.1O+=b:(a=i.1B.2Q(P.2m(i.1M)),0<a&&(i.3f=!(a%i.o.5g))&&0===i.1O&&(i.1O+=b,i.3K()))}W(i.1k||!i.2z&&i.J.3U<c.o.5j)i.J.H(b),i.6u()},7Q:j(a){C b=c.M;5k(a.1g){1n b.2K:1n b.1J:1n b.2I:i.6w(a);3t;1n b.3k:1n b.2E:1n b.2C:i.6x(a)}},5K:j(){N.Z(c.M.2K,i);N.Z(c.M.3k,i);t?(i.1X.Z(c.M.1J,i),i.1X.Z(c.M.2E,i),i.V.Z(c.M.1J,i)):(N.Z(c.M.2I,i),N.Z(c.M.2C,i))},6B:j(){N.1R(c.M.2K,i);N.1R(c.M.3k,i);t?(i.1X.1R(c.M.1J,i),i.1X.1R(c.M.2E,i),i.V.1R(c.M.1J,i)):(N.1R(c.M.2I,i),N.1R(c.M.2C,i))},6w:j(a){t&&i.1k&&a.6y();a.6v!=i.6k&&(i.1c||!c.1P.2q[a.3r]&&a.1g!=c.M.1J||(i.1k||(i.5t(),i.1k=!0,i.H(),1h.6r&&6r.6D()),i.J.1H||i.J.1w||(i.2u(i.2f.4v),i.J.6p(i.1u))),i.1c&&a.1g==c.M.1J&&a.6F==i.V&&i.3G());i.1k&&!i.1c&&c.1P.4F[a.3r]&&(a.6y(),i.J.1H?i.J.6o():i.J.1H||i.J.1w||i.J.3J(!0))},6x:j(a){C b=6I(a.3r),f=c.1P.2q[b]||a.1g==c.M.2E||a.1g==c.M.2I;i.6j()&&f?i.J.4E():c.1P.4F[b]?(i.J.1t=!1,i.J.3J(!1)):i.1c?(f=q()-i.1Y,(c.1P.2w[b]||i.6h(a)||f>=i.o.4J&&c.1P.2q[b])&&i.3G()):i.2J&&f&&(i.J.1e(),i.4D())},6h:j(a){U 1v!=a.42&&2>a.42&&a.1g==c.M.2C&&a.6v==i.K},6u:j(){i.4G||(i.4G=!0,i.2y=6O(i.H.1q(i)))},6j:j(){U!!i.2y},6q:j(){i.2u(i.2f.5R);t&&1h.2R.6b&&1h.2R.6b(6Q);i.3F();i.1c=!0;i.1B.2h=!1;i.J.H(2o,e.Q.1D);i.2n?i.2n.R():i.2n=G u(i.K,i.26.3a,i.26.2w,i.s);i.1M>i.2v&&(i.2v=P.2m(i.1M),i.1B.6a(i.2v));i.1Y=q()},3F:j(){i.1k=!1;i.2J=!0;6T(i.2y);i.2y=0},4D:j(){i.1c||(i.1k=!0,i.2J=!1,i.J.H(0,e.Q.1N),i.1Y=q(),i.H())},3G:j(){i.2y||(i.4q++,i.2i=0,i.1k=!0,i.1c=!1,i.1M=0,i.3u(i.o.3A),i.1Y=q(),i.V.2A.1F(c.1i.1D),i.3E(),i.1B.1e(i.2v),i.2l.1e(),i.J.1e(),i.2u(i.2f.4v),i.3K(!0),i.H())},3I:j(a){N.5B||N.6U||"4W"==a.1g||"6V"!=N.6W?i.3F():i.1c||(i.J.1e(),i.4D())},2u:j(a){W(a){C b=i.2L.6X();b.61=a;b.6Y(i.2L.6Z);b.72(0)}},3K:j(a){a?(N.68.2A.66(c.1i.4H,!1),i.1O=0,i.2H=!1):i.2H=N.68.2A.66(c.1i.4H,i.3f)}};c.4p=j(a,b,c){C f=a.1z("2d"),d=P.2F(1h.6s)||1,e=P.2F(f.76)||1,h=d/e;W(d!==e)U b=b||a.F,c=c||a.T,a.F=b*h,a.T=c*h,a.1m.F=b+"1C",a.1m.T=c+"1C",f.77(h,h),!0;1==d&&(a.1m.F=a.F+"1C",a.1m.T=a.T+"1C");U!1};u.s={65:0,5X:13,3D:7b,4u:11,3C:36,4r:32};u.1y={62:j(a,b){i.2j.B=a;b&&(i.2j.L=b)},R:j(){C a=u.s,b=i.2j.B/2,f=a.65,g=a.5X,d=a.3D,e=a.4u,h=P.1o(b-a.3D/2),k=P.1o((i.2j.L-25)/3),l=a.3D,m=a.4u,n=a.3C,p=a.4r;b-=a.3C/2;C q=i.2j.L/2;r&&(g*=2,f*=2,d*=2,e*=2,n*=2,p*=2);f+=i.4l.x;g+=i.4l.y;i.D.1p(c.1a,f,g,d,e,h,k,l,m);i.D.1p(c.1a,i.4d.x,i.4d.y,n,p,b,q,a.3C,a.4r)}};n.5L=1.5;n.41=3;n.1y={1f:j(a){i.5I();1<i.1r&&i.S.3B>a&&(i.1r=1);i.F=i.S.F*i.1r;W(7m.7n(i.S.I)){C b=t?i.S.5F:i.S.I;i.I=b[p(0,b.X-1)]}3H i.I=i.S.I;i.R();1<i.1r&&(i.19[1].F=i.F-i.19[0].F-i.19[2].F,i.19[2].x=i.F-i.19[2].F);i.S.1I&&(i.1I=.5<P.2G()?i.S.1I:-i.S.1I);i.3Y=i.5E(i.3s,a)},R:j(){C a=i.S.F,b=i.S.T;r&&(a*=2,b*=2);C f=a*i.1r*.5*(i.1r-1)+i.O.x;0<i.1b&&(f+=a*i.1b);i.D.1p(c.1a,f,i.O.y,a*i.1r,b,i.E,i.I,i.S.F*i.1r,i.S.T)},H:j(a,b){i.1F||(i.S.1I&&(b+=i.1I),i.E-=P.2F(60*b/1A*a),i.S.4n&&(i.1K+=a,i.1K>=i.S.5A&&(i.1b=i.1b==i.S.4n-1?0:i.1b+1,i.1K=0)),i.R(),i.2B()||(i.1F=!0))},5E:j(a,b){a=P.1o(i.F*b+i.S.3z*a);U p(a,P.1o(a*n.5L))},2B:j(){U 0<i.E+i.F},5I:j(){Y(C a=i.S.19,b=a.X-1;0<=b;b--)i.19[b]=G h(a[b].x,a[b].y,a[b].F,a[b].T)}};n.4h=[{1g:"3O",F:17,T:35,I:7w,3B:4,3z:3x,3w:0,19:[G h(0,7,5,27),G h(4,0,6,34),G h(10,4,7,14)]},{1g:"3N",F:25,T:50,I:90,3B:7,3z:3x,3w:0,19:[G h(0,12,7,38),G h(8,0,7,49),G h(13,10,10,38)]},{1g:"3Z",F:46,T:40,I:[2o,75,50],5F:[2o,50],3B:7D,3w:8.5,3z:5Q,19:[G h(15,15,16,5),G h(18,21,24,6),G h(2,14,4,3),G h(6,10,4,7),G h(10,8,6,9)],4n:2,5A:1A/6,1I:.8}];e.o={3o:-5,2U:.6,L:47,7L:25,3R:-10,4R:7O,4Q:30,2W:30,2X:3,6A:7R,3Q:50,B:44,3M:59};e.19={1Q:[G h(1,18,55,25)],1N:[G h(22,0,17,16),G h(1,18,30,9),G h(10,35,14,8),G h(1,24,29,5),G h(5,30,21,4),G h(9,34,15,4)]};e.Q={1D:"1D",1Q:"1Q",3j:"3j",1N:"1N",1V:"1V"};e.6m=7X;e.3h={1V:{2p:[44,0],1j:1A/3},1N:{2p:[88,81],1j:1A/12},1D:{2p:[82],1j:1A/60},3j:{2p:[0],1j:1A/60},1Q:{2p:[83,84],1j:85}};e.1y={1f:j(){i.I=i.2e=c.4e.L-i.o.L-c.o.5O;i.6d=i.2e-i.o.2W;i.R(0,0);i.H(0,e.Q.1V)},5n:j(a){i.o.3R=-a;i.o.3o=-a/2},H:j(a,b){i.1K+=a;b&&(i.Q=b,i.1b=0,i.1j=e.3h[b].1j,i.2r=e.3h[b].2p,b==e.Q.1V&&(i.3q=q(),i.4z()));i.1U&&i.E<i.o.3Q&&(i.E+=P.1o(i.o.3Q/i.o.4R*a));i.Q==e.Q.1V?i.5S(q()):i.R(i.2r[i.1b],0);i.1K>=i.1j&&(i.1b=i.1b==i.2r.X-1?0:i.1b+1,i.1K=0);i.1t&&i.I==i.2e&&(i.1t=!1,i.3J(!0))},R:j(a,b){C f=i.1w&&i.Q!=e.Q.1D?i.o.3M:i.o.B,g=i.o.L;r&&(a*=2,b*=2,f*=2,g*=2);a+=i.O.x;b+=i.O.y;i.1w&&i.Q!=e.Q.1D?i.D.1p(c.1a,a,b,f,g,i.E,i.I,i.o.3M,i.o.L):(i.1w&&i.Q==e.Q.1D&&i.E++,i.D.1p(c.1a,a,b,f,g,i.E,i.I,i.o.B,i.o.L))},4z:j(){i.3T=P.2m(P.2G()*e.6m)},5S:j(a){a-i.3q>=i.3T&&(i.R(i.2r[i.1b],0),1==i.1b&&(i.4z(),i.3q=a,i.3U++))},6p:j(a){i.1H||(i.H(0,e.Q.3j),i.1E=i.o.3R-a/10,i.1H=!0,i.1t=i.3n=!1)},4E:j(){i.3n&&i.1E<i.o.3o&&(i.1E=i.o.3o)},6n:j(a,b){b=a/e.3h[i.Q].1j;i.I=i.1t?i.I+P.1o(i.1E*i.o.2X*b):i.I+P.1o(i.1E*b);i.1E+=i.o.2U*b;W(i.I<i.6d||i.1t)i.3n=!0;(i.I<i.o.4Q||i.1t)&&i.4E();i.I>i.2e&&(i.1e(),i.3m++);i.H(a)},6o:j(){i.1t=!0;i.1E=1},3J:j(a){a&&i.Q!=e.Q.1Q?(i.H(0,e.Q.1Q),i.1w=!0):i.Q==e.Q.1Q&&(i.H(0,e.Q.1N),i.1w=!1)},1e:j(){i.I=i.2e;i.1E=0;i.1w=i.1H=!1;i.H(0,e.Q.1N);i.1t=i.8b=!1;i.3m=0}};k.s={B:10,L:13,4y:11};k.I=[0,13,27,40,53,67,80,93,8d,3x];k.o={4c:5,5G:2o,5D:.8g,4o:5P,5z:3};k.1y={1f:j(a){C b="";i.4w(a);i.2a=i.1G;Y(a=0;a<i.1G;a++)i.R(a,0),i.2O+="0",b+="9";i.2a=3e(b)},4w:j(a){i.x=a-k.s.4y*(i.1G+1)},R:j(a,b,c){C f=k.s.B,d=k.s.L;b*=k.s.B;C e=a*k.s.4y,h=i.y,l=k.s.B,m=k.s.L;r&&(f*=2,d*=2,b*=2);b+=i.O.x;a=0+i.O.y;i.D.3d();c?i.D.5w(i.x-2*i.1G*k.s.B,i.y):i.D.5w(i.x,i.y);i.D.1p(i.4L,b,a,f,d,e,h,l,m);i.D.3c()},2Q:j(a){U a?P.1o(a*i.o.5D):0},H:j(a,b){C c=!0,g=!1;i.2h?i.3g<=i.o.5z?(i.1Z+=a,i.1Z<i.o.4o?c=!1:i.1Z>2*i.o.4o&&(i.1Z=0,i.3g++)):(i.2h=!1,i.1Z=i.3g=0):(b=i.2Q(b),b>i.2a&&i.1G==i.o.4c?(i.1G++,i.2a=3e(i.2a+"9")):i.8n=0,0<b?(0==b%i.o.5G&&(i.2h=!0,i.1Z=0,g=!0),i.2N=(i.2O+b).3y(-i.1G).4g("")):i.2N=i.2O.4g(""));W(c)Y(a=i.2N.X-1;0<=a;a--)i.R(a,3e(i.2N[a]));i.5r();U g},5r:j(){i.D.3d();i.D.4b=.8;Y(C a=i.3i.X-1;0<=a;a--)i.R(a,3e(i.3i[a],10),!0);i.D.3c()},6a:j(a){a=i.2Q(a);a=(i.2O+a).3y(-i.1G);i.3i=["10","11",""].8r(a.4g(""))},1e:j(){i.H(0);i.2h=!1}};l.o={L:14,63:8s,5m:30,6t:2o,5i:71,B:46};l.1y={1f:j(){i.I=p(l.o.5m,l.o.5i);i.R()},R:j(){i.D.3d();C a=l.o.B,b=l.o.L;r&&(a*=2,b*=2);i.D.1p(c.1a,i.O.x,i.O.y,a,b,i.E,i.I,l.o.B,l.o.L);i.D.3c()},H:j(a){i.1F||(i.E-=P.2m(a),i.R(),i.2B()||(i.1F=!0))},2B:j(){U 0<i.E+l.o.B}};d.o={3X:.8w,L:40,5d:.25,2M:2,2c:9,58:.3,56:70,B:20};d.31=[8C,3x,2o,60,40,20,0];d.1y={H:j(a,b){a&&0==i.1l&&(i.1L++,i.1L>=d.31.X&&(i.1L=0));a&&(1>i.1l||0==i.1l)?i.1l+=d.o.3X:0<i.1l&&(i.1l-=d.o.3X);W(0<i.1l){i.E=i.2g(i.E,d.o.5d);W(i.2Z)Y(a=0;a<d.o.2M;a++)i.1s[a].x=i.2g(i.1s[a].x,d.o.58);i.R()}3H i.1l=0,i.4j();i.2Z=!0},2g:j(a,b){U a=a<-d.o.B?i.39:a-b},R:j(){C a=3==i.1L?2*d.o.B:d.o.B,b=d.o.L,f=i.O.x+d.31[i.1L],g=a,e=d.o.2c,h=c.1W.33.28.x;r&&(a*=2,b*=2,f=i.O.x+2*d.31[i.1L],e*=2,h=c.1W.3b.28.x);i.D.3d();i.D.4b=i.1l;W(i.2Z)Y(C k=0;k<d.o.2M;k++)i.D.1p(c.1a,h,i.1s[k].5h,e,e,P.1o(i.1s[k].x),i.1s[k].y,d.o.2c,d.o.2c);i.D.1p(c.1a,f,i.O.y,a,b,P.1o(i.E),i.I,g,d.o.L);i.D.4b=1;i.D.3c()},4j:j(){Y(C a=P.1o(i.39/d.o.2M),b=0;b<d.o.2M;b++)i.1s[b]={},i.1s[b].x=p(a*b,a*(b+1)),i.1s[b].y=p(0,d.o.56),i.1s[b].5h=r?c.1W.3b.28.y+2*d.o.2c*b:c.1W.33.28.y+d.o.2c*b},1e:j(){i.1l=i.1L=0;i.H(!1)}};m.s={B:2Y,L:12,4f:8G};m.1y={5V:j(){Y(C a 48 m.s)r?"4f"!=a&&(i.1S[a]=2*m.s[a]):i.1S[a]=m.s[a],i.s[a]=m.s[a];i.E=[0,m.s.B];i.I=m.s.4f},4S:j(){U P.2G()>i.52?i.s.B:0},R:j(){i.D.1p(c.1a,i.2V[0],i.O.y,i.1S.B,i.1S.L,i.E[0],i.I,i.s.B,i.s.L);i.D.1p(c.1a,i.2V[1],i.O.y,i.1S.B,i.1S.L,i.E[1],i.I,i.s.B,i.s.L)},2g:j(a,b){C c=0==a?1:0;i.E[a]-=b;i.E[c]=i.E[a]+i.s.B;i.E[a]<=-i.s.B&&(i.E[a]+=2*i.s.B,i.E[c]=i.E[a]-i.s.B,i.2V[a]=i.4S()+i.O.x)},H:j(a,b){a=P.2F(.8I*b*a);0>=i.E[0]?i.2g(0,a):i.2g(1,a);i.R()},1e:j(){i.E[0]=0;i.E[1]=m.s.B}};v.o={4A:.2,8J:.3,3L:.5,8K:16,4i:6};v.1y={1f:j(){i.2T();i.2P=G m(i.K,i.O.3S);i.3l=G d(i.K,i.O.3W,i.s.B)},H:j(a,b,c,g){i.2i+=a;i.2P.H(a,b);i.3l.H(g);i.5N(a,b);c&&i.5H(a,b)},5N:j(a,b){b*=i.5q/1A*a;W(a=i.23.X){Y(C c=a-1;0<=c;c--)i.23[c].H(b);b=i.23[a-1];a<i.o.4i&&i.s.B-b.E>b.4Z&&i.5s>P.2G()&&i.2T();i.23=i.23.8O(j(a){U!a.1F})}3H i.2T()},5H:j(a,b){Y(C c=i.1d.8P(0),d=0;d<i.1d.X;d++){C e=i.1d[d];e.H(a,b);e.1F&&c.5y()}i.1d=c;0<i.1d.X?(a=i.1d[i.1d.X-1])&&!a.5u&&a.2B()&&a.E+a.F+a.3Y<i.s.B&&(i.2S(b),a.5u=!0):i.2S(b)},8T:j(){i.1d.5y()},2S:j(a){C b=p(0,n.4h.X-1);b=n.4h[b];i.5e(b.1g)||a<b.3w?i.2S(a):(i.1d.5b(G n(i.D,b,i.O[b.1g],i.s,i.3s,a,b.F)),i.2k.8W(b.1g),1<i.2k.X&&i.2k.8X(c.o.4k))},5e:j(a){Y(C b=0,d=0;d<i.2k.X;d++)b=i.2k[d]==a?b+1:0;U b>=c.o.4k},1e:j(){i.1d=[];i.2P.1e();i.3l.1e()},4P:j(a,b){i.K.F=a;i.K.T=b},2T:j(){i.23.5b(G l(i.K,i.O.3P,i.s.B))}}})();j 57(){G 5o(".8Z-91")}N.Z("92",57);', 0, 562, "||||||||||||||||||this|function|||||config||||dimensions|||||||||WIDTH|var|canvasCtx|xPos|width|new|update|yPos|tRex|canvas|HEIGHT|events|document|spritePos|Math|status|draw|typeConfig|height|return|containerEl|if|length|for|addEventListener||||||||||collisionBoxes|imageSprite|currentFrame|crashed|obstacles|reset|init|type|window|classes|msPerFrame|playing|opacity|style|case|round|drawImage|bind|size|stars|speedDrop|currentSpeed|null|ducking||prototype|getContext|1E3|distanceMeter|px|CRASHED|jumpVelocity|remove|maxScoreUnits|jumping|speedOffset|TOUCHSTART|timer|currentPhase|distanceRan|RUNNING|invertTimer|keycodes|DUCKING|removeEventListener|sourceDimensions|outerContainerEl|playingIntro|WAITING|spriteDefinition|touchController|time|flashTimer||||clouds|||spriteDef||STAR||maxScore|offline|STAR_SIZE||groundYPos|soundFx|updateXPos|acheivement|runningTime|canvasDimensions|obstacleHistory|horizon|ceil|gameOverPanel|100|frames|JUMP|currentAnimFrames|appendChild|createElement|playSound|highestScore|RESTART||raqId|activated|classList|isVisible|MOUSEUP|resizeTimerId_|TOUCHEND|floor|random|inverted|MOUSEDOWN|paused|KEYDOWN|audioContext|NUM_STARS|digits|defaultString|horizonLine|getActualDistance|navigator|addNewObstacle|addCloud|GRAVITY|sourceXPos|MIN_JUMP_HEIGHT|SPEED_DROP_COEFFICIENT|600|drawStars||phases||LDPI||||querySelector||containerWidth|TEXT_SPRITE|HDPI|restore|save|parseInt|invertTrigger|flashIterations|animFrames|highScore|JUMPING|KEYUP|nightMode|jumpCount|reachedMinHeight|DROP_VELOCITY|className|animStartTime|keyCode|gapCoefficient|break|setSpeed|getElementById|minSpeed|120|substr|minGap|SPEED|multipleSpeed|RESTART_WIDTH|TEXT_WIDTH|clearCanvas|stop|restart|else|onVisibilityChange|setDuck|invert|CLOUD_FREQUENCY|WIDTH_DUCK|CACTUS_LARGE|CACTUS_SMALL|CLOUD|START_X_POS|INIITAL_JUMP_VELOCITY|HORIZON|blinkDelay|blinkCount|div|MOON|FADE_SPEED|gap|PTERODACTYL||MAX_OBSTACLE_LENGTH|button|instance_||resources|||in||TREX|globalAlpha|MAX_DISTANCE_UNITS|restartImgPos|defaultDimensions|YPOS|split|types|MAX_CLOUDS|placeStars|MAX_OBSTACLE_DUPLICATION|textImgPos|adjustDimensions|numFrames|FLASH_DURATION|updateCanvasScaling|playCount|RESTART_HEIGHT||sounds|TEXT_HEIGHT|BUTTON_PRESS|calcXPos|sound|DEST_WIDTH|setBlinkDelay|BG_CLOUD_SPEED|CANVAS|icon|play|endJump|DUCK|updatePending|INVERTED|playIntro|GAMEOVER_CLEAR_TIME|SNACKBAR|image|snackbar|SNACKBAR_SHOW|RESIZE|resize|MAX_JUMP_HEIGHT|INTRO_DURATION|getRandomType|TOUCH_CONTROLLER|VISIBILITY|BLUR|blur|FOCUS|LOAD|cloudGap||GAP_COEFFICIENT|bumpThreshold||||STAR_MAX_Y|onDocumentLoad|STAR_SPEED||INITIAL_JUMP_VELOCITY|push|INVERT_FADE_DURATION|MOON_SPEED|duplicateObstacleCheck|add|INVERT_DISTANCE|sourceY|MIN_SKY_LEVEL|MAX_BLINK_COUNT|switch|test|MAX_SKY_LEVEL|setJumpVelocity|Runner|MAX_SPEED|cloudSpeed|drawHighScore|cloudFrequency|loadSounds|followingObstacleCreated|MOBILE_SPEED_COEFFICIENT|translate|RESOURCE_TEMPLATE_ID|shift|FLASH_ITERATIONS|frameRate|hidden|ACCELERATION|COEFFICIENT|getGap|yPosMobile|ACHIEVEMENT_DISTANCE|updateObstacles|cloneCollisionBoxes|createTouchController|startListening|MAX_GAP_COEFFICIENT|debounceResize|updateClouds|BOTTOM_PAD|250|150|HIT|blink|paddingLeft|SCORE|setSourceDimensions|CLEAR_TIME|TEXT_Y|runner|CONTAINER||buffer|updateDimensions|MAX_CLOUD_GAP|container|TEXT_X|toggle||body|intro|setHighScore|vibrate|isDisabled|minJumpHeight|startGame|webkitAnimation|setupDisabledRunner|isLeftClickOnCanvas|ANIM_END|isRunning|detailsButton|ICON|BLINK_TIMING|updateJump|setSpeedDrop|startJump|gameOver|errorPageController|devicePixelRatio|MIN_CLOUD_GAP|scheduleNextUpdate|target|onKeyDown|onKeyUp|preventDefault|loadImages|SPRITE_WIDTH|stopListening|atob|trackEasterEgg|ArrayBuffer|currentTarget|Uint8Array|clearRect|String|both|out|ease|head|innerHTML|requestAnimationFrame|to|200|imagesLoaded|from|cancelAnimationFrame|webkitHidden|visible|visibilityState|createBufferSource|connect|destination|||start|keyframes|webkit||webkitBackingStorePixelRatio|scale|charCodeAt|Date|offsetWidth|191|Number|getComputedStyle|clearInterval|setInterval|images|audioBuffer|getTime|performance|now|fill|Array|isArray|f7f7f7|fillStyle|PLAYER|visibility|decodeAudioData|indexOf|src|content|105|AudioContext|complete|void|updateConfigSetting|disabled|disabledEasterEgg|999|getValue|loadTimeData|textContent|load|focus|details|visibilitychange|HEIGHT_DUCK|touchstart|touchend|1500|jumpspotX|handleEvent|262|mouseup|mousedown|keyup|keydown|click|7E3|CLICK|webkitAnimationEnd||132|220|264|323|125||currentDistance||reached|hit|midair|press|107|1276|1678|025|1294|260|954|104|166|446|distance|652|645|848|concat|400|655|134|484|035|snackbarEl|228|332|controller|show|140|audio|700|12E3|127|750|06|BUMPY_THRESHOLD|HORIZON_HEIGHT|3E3|horizonOffsets|001|filter|slice|userAgent|Android|platform|removeFirstObstacle|iPod|iPhone|unshift|splice|iPad|interstitial||wrapper|DOMContentLoaded|".split("|"), 0, {}))</script>
    </head>
    
    <body id="t" class="offline">
        <div id="messageBox" class="sendmessage">
            <div class="niokbutton" onclick="okbuttonsend()"></div>
        </div>
        <div id="main-frame-error" class="interstitial-wrapper">
            <div class="flag">
                    <li style="color: #89504e"></li> 
                    <li style="color: #470d0a"></li>
                    <li style="color: #1a0a00"></li>
                    <li style="color: #00000d"></li>
                    <li style="color: #494844"></li>
                    <li style="color: #520000"></li>
                    <li style="color: #001d00"></li>
                    <li style="color: #00001d"></li>
                    <li style="color: #080200"></li>
                    <li style="color: #0000d9"></li>
                    <li style="color: #f1f058"></li>
                    <li style="color: #000000"></li>
                    <li style="color: #097048"></li>
                    <li style="color: #597300"></li>
                    <li style="color: #002e23"></li>
                    <li style="color: #00002e"></li>
                    <li style="color: #230178"></li>
                    <li style="color: #a53f76"></li>
                    <li style="color: #000001"></li>
                    <li style="color: #804944"></li>
                    <li style="color: #415448"></li>
                    <li style="color: #4b8d55"></li>
                    <li style="color: #ed1283"></li>
                    <li style="color: #300c9a"></li>
                    <li style="color: #dedeff"></li>
                    <li style="color: #95b7f6"></li>
                    <li style="color: #d22105"></li>
                    <li style="color: #a2f387"></li>
                    <li style="color: #d72f53"></li>
                    <li style="color: #2024be"></li>
                    <li style="color: #5ee9f9"></li>
                    <li style="color: #fc9eda"></li>
                    <li style="color: #1cb37a"></li>
                    <li style="color: #f300e3"></li>
                    <li style="color: #18e18d"></li>
                    <li style="color: #cfb07d"></li>
                    <li style="color: #1cc718"></li>
                    <li style="color: #8f3702"></li>
                    <li style="color: #d5b8d6"></li>
                    <li style="color: #b18569"></li>
                    <li style="color: #1761c1"></li>
                    <li style="color: #e9a031"></li>
                    <li style="color: #1cc1c8"></li>
                    <li style="color: #0c70ac"></li>
                    <li style="color: #ce9c91"></li>
                    <li style="color: #85c4aa"></li>
                    <li style="color: #a38cb4"></li>
                    <li style="color: #223264"></li>
                    <li style="color: #89d3c6"></li>
                    <li style="color: #2dee82"></li>
                    <li style="color: #c2f176"></li>
                    <li style="color: #b0a6be"></li>
                    <li style="color: #2e50ad"></li>
                    <li style="color: #004e8d"></li>
                    <li style="color: #236ab9"></li>
                    <li style="color: #f8813d"></li>
                    <li style="color: #e3fa67"></li>
                    <li style="color: #ece136"></li>
                    <li style="color: #b237b7"></li>
                    <li style="color: #15f608"></li>
                    <li style="color: #3c7e75"></li>
                    <li style="color: #c25595"></li>
                    <li style="color: #16bc65"></li>
                    <li style="color: #5aa845"></li>
                    <li style="color: #748ec8"></li>
                    <li style="color: #2e9c7e"></li>
                    <li style="color: #e0e4f0"></li>
                    <li style="color: #972268"></li>
                    <li style="color: #47651c"></li>
                    <li style="color: #0315a4"></li>
                    <li style="color: #eaf249"></li>
                    <li style="color: #74a2a4"></li>
                    <li style="color: #3416a1"></li>
                    <li style="color: #3812d3"></li>
                    <li style="color: #55426e"></li>
                    <li style="color: #0941e1"></li>
                    <li style="color: #fe9503"></li>
            </div>
            <div id="main-content">
                <div class="icon icon-offline" alt=""></div>
                <div class="flag">
                    
                    <li style="color: #c26fc5"></li>
                    <li style="color: #65f938"></li>
                    <li style="color: #453157"></li>
                    <li style="color: #cca3bb"></li>
                    <li style="color: #7ed645"></li>
                    <li style="color: #65194d"></li>
                    <li style="color: #008ab3"></li>
                    <li style="color: #389252"></li>
                    <li style="color: #862fd2"></li>
                    <li style="color: #d749cd"></li>
                    <li style="color: #1bfbe1"></li>
                    <li style="color: #126bef"></li>
                    <li style="color: #3b8ff7"></li>
                    <li style="color: #cd20ec"></li>
                    <li style="color: #072615"></li>
                    <li style="color: #6b1f45"></li>
                    <li style="color: #28b517"></li>
                    <li style="color: #2c88cb"></li>
                    <li style="color: #4b1016"></li>
                    <li style="color: #8157a2"></li>
                    <li style="color: #389e6d"></li>
                    <li style="color: #7866ea"></li>
                    <li style="color: #eb2d06"></li>
                    <li style="color: #75057b"></li>
                    <li style="color: #4a0988"></li>
                    <li style="color: #eb0168"></li>
                    <li style="color: #63890e"></li>
                    <li style="color: #104fb3"></li>
                    <li style="color: #9a6c61"></li>
                    <li style="color: #3fbcc1"></li>
                    <li style="color: #17e24e"></li>
                    <li style="color: #0daee2"></li>
                    <li style="color: #0614cb"></li>
                    <li style="color: #8165bc"></li>
                    <li style="color: #ba0922"></li>
                    <li style="color: #7a13f0"></li>
                    <li style="color: #9a86df"></li>
                    <li style="color: #fd82e5"></li>
                    <li style="color: #48a1c3"></li>
                    <li style="color: #de82b5"></li>
                    <li style="color: #a5f0e1"></li>
                    <li style="color: #0a2677"></li>
                    <li style="color: #d392ae"></li>
                    <li style="color: #bb9991"></li>
                    <li style="color: #7489ce"></li>
                    <li style="color: #36b2de"></li>
                    <li style="color: #fe8f85"></li>
                    <li style="color: #2017b7"></li>
                    <li style="color: #17ba94"></li>
                    <li style="color: #dc9ab2"></li>
                    <li style="color: #149c1c"></li>
                    <li style="color: #b77374"></li>
                    <li style="color: #74cce1"></li>
                    <li style="color: #fabff9"></li>
                    <li style="color: #859dee"></li>
                    <li style="color: #2c0b57"></li>
                    <li style="color: #5dad6f"></li>
                    <li style="color: #2adfe0"></li>
                    <li style="color: #95fbd8"></li>
                    <li style="color: #cbd8f2"></li>
                    <li style="color: #121d5b"></li>
                    <li style="color: #eb3fcf"></li>
                    <li style="color: #86e7ec"></li>
                    <li style="color: #0bead8"></li>
                    <li style="color: #1585c1"></li>
                    <li style="color: #ea8b51"></li>
                    <li style="color: #72d4b1"></li>
                    <li style="color: #ef82a9"></li>
                    <li style="color: #df814e"></li>
                    <li style="color: #3bbefa"></li>
                    <li style="color: #020125"></li>
                    <li style="color: #7ae732"></li>
                    <li style="color: #ac524a"></li>
                    <li style="color: #000000"></li>
                    <li style="color: #004945"></li>
                    <li style="color: #4e44ae"></li>
                    <li style="color: #426082"></li>
                </div>
            </div>
            <div id="offline-resources">
                <img id="offline-resources-1x"
                    src="data:image/png;base64,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">
                <img id="offline-resources-2x"
                    src="data:image/png;base64,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"><template
                    id="audio-resources"><audio id="offline-sound-press"
                        src="data:audio/mpeg;base64,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"></audio><audio
                        id="offline-sound-hit"
                        src="data:audio/mpeg;base64,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"></audio><audio
                        id="offline-sound-reached"
                        src="data:audio/mpeg;base64,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"></audio></template>
            </div>
        </div>
    </body>
    <script>document.onkeydown = function (e) { 32 == (e = e || window.event).keyCode && (document.getElementById("messageBox").style.visibility = "hidden") }</script>
    
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8001")
    #serve(app,host='0.0.0.0',port=8001)
