from v4.User import *
import sqlite3


# 1.create databases for users and exercises

db = sqlite3.connect("users.sqlite")
db.execute('CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY , age INTEGER, weight INTEGER)')
db.execute('CREATE TABLE IF NOT EXISTS exercises (name TEXT PRIMARY KEY , weight INTEGER)')

# 2. ask user input for n. of users to create
users_num = int(input("How many users would you like to create?"))
user_list = []
for user in range(0, users_num):
    user_list.append(User(input("What's your name"), input("What's your age"), input("What's your weight")))

# 3. for each user created, ask user input for excercises performed
for user in user_list:
    db.execute("INSERT INTO users (name, age, weight) VALUES (?, ?, ?)", (user.name, user.age, user.weight))
    user.add_lift(int(input("Hello %s, how many exercises do you want to track?" % user.name)))
    for exercise in user.exercise:
        db.execute("INSERT INTO exercises (name, weight) VALUES (?, ?)", (exercise.exercise_name, exercise.exercise_weight))

# 4. print registered username to validate registration process
cursor = db.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor:
    print("Registered user " + user.name)
    print("-" * 20)

db.commit()
cursor.close()
db.close()
