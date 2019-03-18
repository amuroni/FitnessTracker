"""this will contain User attributes, connected to the exercises he does"""
from v1.Exercise import Exercise


class User:

    def __init__(self, name, age, weight):  # main user attrs
        self.name = name
        self.age = age
        self.weight = weight
        self.exercise = Exercise  # composition instead of inheritance, more logical in this case
        self.user_exercises = []

    def presentation(self):
        print("User %s is %s years old and weighs %s kg" % (self.name, self.age, self.weight))

    def add_lift(self, exercise):
        exercise_number = int(input("How many exercises would you like to add?"))
        for i in range(0, exercise_number):
            self.user_exercises.append(Exercise(input("What exercise did you do ?"), input("With how much weight?")))
        print(self.name + " tracked a " + exercise.name + " at " + exercise.weight)
