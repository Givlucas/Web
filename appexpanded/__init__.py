from flask import Flask, render_template
from flask_mobility import Mobility
import socket, sys
import six
def send(x):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("192.168.1.31", 6020))
    freq = int(x)
    c = 0
    buf = ""

    while freq > 0:
            c += 1
            buf = buf + chr(freq & 0xff)
            freq = freq >> 8

    s.send(six.b(buf))
    s.close()

app = Flask(__name__)
Mobility(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/1027')
def station1():
    send(102700000)
    return("nothing")

@app.route('/999')
def station2():
    send(99900000)
    return("nothing")

@app.route('/961')
def station3():
    send(96100000)
    return("nothing")

@app.route('/1073')
def station4():
    send(107300000)
    return("nothing")


if __name__ == "__main__":
    app.run()
