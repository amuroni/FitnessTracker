"""this will automate the process of user creation, creating a specific n of accounts"""
from v1.User import User


def create_user(account_number):
    # user_list = []
    # account_number = int(input("How many accounts would you like to create?"))
    global user
    for i in range(0, account_number):
        user_name = input("What's your name")
        user_age = input("What's your age")
        user_weight = input("What's your weight")
        user = User(user_name, user_age, user_weight)
    return user
