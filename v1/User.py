"""this will contain User attributes, connected to the exercises he does"""
from v1.Exercise import Exercise


class User:

    def __init__(self, name, age, weight):  # main user attrs
        self.name = name
        self. age = age
        self.weight = weight
        self.exercise = Exercise

    def presentation(self):
        print("User %s is %s years old and weighs %s kg" % (self.name, self.age, self.weight))

    def add_lift(self, exercise):
        self.user_lifts = [exercise]
        print(self.name + " just did a " + exercise.name + " at " + exercise.weight)
