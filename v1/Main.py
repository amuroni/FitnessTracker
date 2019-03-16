"""main app file"""

from v1.classes import User

user1 = User(input("What's your name"), input("What's your age"), input("WHat's your weight?"))
user1.presentation()
