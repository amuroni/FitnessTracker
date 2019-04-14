"""this will contain User attributes, connected to the exercises he does"""
from v1.Exercise import Exercise


class User:

    def __init__(self, name, age, weight):  # main user attrs
        self.name = name
        self.age = age
        self.weight = weight
        self.exercise = []

    # def presentation(self):
    #     print("Registered user %s is %s years old and weighs %s kg" % (self.name, self.age, self.weight))
    #
    # def create_user(self, users_num):
    #     user_list = []  # list containing all the users created and their attrs
    #     for user in range(0, users_num):
    #         self.name = input("What's your name")
    #         self.age = input("What's your age")
    #         self.weight = input("What's your weight")
    #         user_list.append(User(self.name, self.age, self.weight))
    #         # user.add_lift(int(input("How many exercises do you wanna track?")))
    #     return user_list

    def add_lift(self, exercise_number):
        # user_exercises = []
        for exercise in range(0, exercise_number):
            exercise = Exercise(input("What exercise did you do ?"), input("With how much weight?"))
            self.exercise.append(exercise)
        return self.exercise
