"""main app file - v2_flask will focus on implementing user management via Flask-login"""
from v2_flask.app.models import *
from flask import Blueprint, render_template
from v2_flask.app import app
main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
def profile():
    return render_template("profile.html")


users_num = int(input("How many users would you like to create?"))
user_list = []
for user in range(0, users_num):
    user_list.append(User(input("What's your name"), input("What's your age"), input("What's your weight")))
for user in user_list:
    user.add_lift(int(input("Hello %s, how many exercises do you want to track?" % user.name)))
for user in user_list:
    name = user.name
    for exercise in user.exercise:
        print(name + " " + exercise.exercise_name + " " + exercise.exercise_weight)
