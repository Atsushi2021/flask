# flaskを使う宣言
from flask import Flask,render_template


app=Flask(__name__)


# ルーティング
@app.route("/")
def hello():
    return "HELLO FlASK"


@app.route("/atsushi")
def flask_name():
    return "flask"


@app.route("/sushi")
def sushi():
    neta = "えんがわ"
    return  "好きなネタは" +neta+ "です"


@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/fruit")
def fruit():
    fruit = "みかん"
    return render_template("index.html",tpl_fruit=fruit)
                                        # 左側tpl_fruitがhtml側に書く　　fruitはpython側の変数


if __name__ == "__main__":
    app.run(debug=True)