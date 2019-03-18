"""main app file - v1 will focus on assigning attributes and gathering + showing data to the user"""

from v1.User import *
# from v1.Exercise import *

# user1 = User(input("What's your name"), input("What's your age"), input("What's your weight?"))
# user_list.presentation()
# exercise1 = Exercise(input("What exercise did you do first?"), input("With how much weight?"))
# exercise2 = Exercise(input("What exercise did you do for second?"), input("With how much weight?"))
# exercise3 = Exercise(input("What exercise did you do the third time?"), input("With how much weight?"))
# user1.add_lift(exercise1)
# user1.add_lift(exercise2)
# user1.add_lift(exercise3)

create_user(int(input("How many users would you like to create?")))  # does not create a user obj?
user1 = User("a", "1", "3")  # actually creates a user obj
# note for future self -> check differences and build the def accordingly
