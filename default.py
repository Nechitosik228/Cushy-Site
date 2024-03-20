from app import app
from flask import render_template, request


@app.route("/cushy")
def cushy():
    return render_template("_base.html")

@app.route("/cushy/account")
def account():
    return render_template("_account.html")

@app.route("/cushy/stop_shopping")
def stop_shopping():
     return render_template("_stop_shopping.html")

@app.route("/cushy/buy")
def buy():
    return render_template("_buy.html")