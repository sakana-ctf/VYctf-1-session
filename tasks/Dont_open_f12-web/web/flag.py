from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    html = r"""
        <!DOCTYPE html>
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
                        time_data = time_data - 1;
	                    setInterval(move,time_data);
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

if __name__ == "__main__":
    app.run()
