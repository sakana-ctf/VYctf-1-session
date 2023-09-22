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
