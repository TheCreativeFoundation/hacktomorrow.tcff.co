from flask import Flask, render_template, redirect, request

# FIREBASE ADMIN SETUP

application = Flask(__name__)

@application.route("/")
def index():
    return redirect("/hackathon")


@application.route("/hackathon")
def hackathon():
    return render_template("hackathon.html")


@application.route("/login")
def login():
    if request.args.get("token"):
        pass
    return render_template("login.html")


@application.route("/join")
def join():
    return render_template("join.html")


if __name__ == "__main__":
    application.run()


