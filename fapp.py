from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/snapCode")
def snapCode():
    return render_template('snapCode.html')

@app.route("/showroom")
def showroom():
    return render_template('showroom/showroom.html')

if __name__ == "__main__":
    app.run(debug=False)
