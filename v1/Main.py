"""main app file - v1 will focus on assigning attributes and gathering + showing data to the user"""

from v1.User import *
from v1.Exercise import *

user1 = User(input("What's your name"), input("What's your age"), input("What's your weight?"))
user1.presentation()

exercise1 = Exercise(input("What exercise did you just do?"), input("With how much weight?"))
user1.add_lift(exercise1)
