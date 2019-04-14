"""Exercise class, with exercise name and weight, reps and sets"""


class Exercise:

    def __init__(self, exercise_name, exercise_weight):
        self.exercise_name = exercise_name
        self.reps = 1
        self.sets = 1
        self.exercise_weight = exercise_weight
