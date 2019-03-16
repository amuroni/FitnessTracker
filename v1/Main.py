"""main app file - v1 will focus on assiging attributes and gathering + showing data to the user"""

from v1.classes import User

user1 = User(input("What's your name"), input("What's your age"), input("WHat's your weight?"))
user1.presentation()
