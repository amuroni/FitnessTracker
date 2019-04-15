from v4.User import *
import sqlite3
import uuid


# 1.create databases for users and exercises

db = sqlite3.connect("database.sqlite")
db.execute('CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT, age INTEGER, weight INTEGER)')
db.execute('CREATE TABLE IF NOT EXISTS exercises (id TEXT PRIMARY KEY, name TEXT, weight INTEGER)')

# 2. ask user input for n. of users to create
users_num = int(input("How many users would you like to create?"))
user_list = []
for user in range(0, users_num):
    user_list.append(User(input("What's your name"), input("What's your age"), input("What's your weight")))

# 3. for each user created, add to db then ask user input for exercises performed and add to db
for user in user_list:
    db.execute("INSERT INTO users (id, name, age, weight) VALUES (?, ?, ?, ?)",  # add each user to db
               (str(uuid.uuid1()), user.name, user.age, user.weight))
    user.add_lift(int(input("Hello %s, how many exercises do you want to track?" % user.name)))
    for exercise in user.exercise:
        db.execute("INSERT INTO exercises (id, name, weight) VALUES (?, ?, ?)",   # add each exercise to db
                   ("placeholder, add user uuid", exercise.exercise_name, exercise.exercise_weight))  # to do: ADD UUID!

# 4. print registered username from db to validate registration process
cursor = db.cursor()
cursor.execute("SELECT * FROM users")
for row in cursor:
    print("Registered user " + user.name)  # weird error check, still works as expected?
    print("-" * 20)

# 5. commit changes and close cursor and db
db.commit()
cursor.close()
db.close()
