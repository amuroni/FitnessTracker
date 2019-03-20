"""main app file - v1 will focus on assigning attributes and gathering + showing data to the user"""
from v1.User import *


# user1 = User(input("What's your name"), input("What's your age"), input("What's your weight?"))
# user_list.presentation()
# exercise1 = Exercise(input("What exercise did you do first?"), input("With how much weight?"))
# exercise2 = Exercise(input("What exercise did you do for second?"), input("With how much weight?"))
# exercise3 = Exercise(input("What exercise did you do the third time?"), input("With how much weight?"))
# user1.add_lift(exercise1)
# user1.add_lift(exercise2)
# user1.add_lift(exercise3)

# users = User.create_user(User, int(input("How many users would you like to create?")))  # does not create a user obj?
# for user in users:
#     user.add_lift(int(input("How many exercises do you wanna track?")))

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
