"""this will contain the main classes of the app"""


class Lift:

    def __init__(self, name, reps=0, sets=0, rpe=0, description=""):
        self.name = name
        self.reps = reps
        self.sets = sets
        self.rpe = rpe
        self.description = description


class User:

    def __init__(self, name="", age="", weight=""):
        self.name = name
        self.age = age
        self.weight = weight

    def presentation(self):
        print("User %s is %s years old and weighs %s kg" % (self.name, self.age, self.weight))
