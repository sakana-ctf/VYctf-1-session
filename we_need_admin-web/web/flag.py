from flask import Flask,request
import os

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def web3_question():
    flag = "据说只要拿到管理员的cookie, flag就会显现<br>"
    if request.cookies.get("admin") == "chinanako":
        flag = "VYctf{X5s_1s_0ur_f1r5t_M4ch1ne_1n_Web}"
    if request.method == "POST":
        flag += request.form['hack']
    html = open("flag.html").read()
    return html.replace("{{flag}}",flag)#render_template("flag.html", flag=eval_data)

if __name__ == "__main__":
    app.run(host="172.24.170.134",port=8000)
