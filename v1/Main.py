"""main app file - v1 will focus on assigning attributes and gathering + showing data to the user"""
from v1.Create_user import create_user

# user1 = User(input("What's your name"), input("What's your age"), input("What's your weight?"))
# user_list.presentation()
# exercise1 = Exercise(input("What exercise did you do first?"), input("With how much weight?"))
# exercise2 = Exercise(input("What exercise did you do for second?"), input("With how much weight?"))
# exercise3 = Exercise(input("What exercise did you do the third time?"), input("With how much weight?"))
# user1.add_lift(exercise1)
# user1.add_lift(exercise2)
# user1.add_lift(exercise3)

user = create_user(int(input("How many users would you like to create?")))  # does not create a user obj?
# user1 = User("a", "1", "3")  # actually creates a user obj
# note for future self -> check differences and build the def accordingly
# i can now create the user with the return statement at the end of create_user
# however, only the last one created is returned, the first one is not kept in memory.
