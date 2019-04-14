"""this will contain User attributes, connected to the exercises he does"""
from v2_flask.app.exercise import Exercise
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    def __init__(self, name, age, weight):  # main user attrs
        self.name = name
        self.age = age
        self.weight = weight
        self.exercise = []

    def add_lift(self, exercise_number):
        # user_exercises = []
        for exercise in range(0, exercise_number):
            exercise = Exercise(input("What exercise did you do ?"), input("With how much weight?"))
            self.exercise.append(exercise)
        return self.exercise

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
