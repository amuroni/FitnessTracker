import sqlite3
import uuid

# 1.create databases for users and exercises

db = sqlite3.connect("database.sqlite")
cursor = db.cursor()
db.execute('CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT, age INTEGER, weight INTEGER)')
db.execute('CREATE TABLE IF NOT EXISTS exercises (id TEXT PRIMARY KEY, name TEXT, weight INTEGER)')

# 2. ask user input for n. of users to create + n. of exercises to add
users_num = int(input("How many users would you like to create?"))
for user in range(0, users_num):
    user_name = input("What's your name")
    cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,))
    if cursor.fetchone() is None:
        user_age = input("What's your age")
        user_weight = input("What's your weight")
        user_id = str(uuid.uuid1())
        db.execute("INSERT INTO users (id, name, age, weight) VALUES (?, ?, ?, ?)",  # add each user attr to db
                   (user_id, user_name, user_age, user_weight))
        db.commit()  # commit the user insert into the users table
        # 2.1 add exercise for each user with the user_id to assign a user to each exercise
        exercise_num = (int(input("Hello %s, how many exercises do you want to track?" % user_name)))
        for exercise in range(0, exercise_num):
            exercise_name = input("What exercise did you do?")
            exercise_weight = input("With hou much weight?")
            exercise_id = user_id
            db.execute("INSERT INTO exercises (id, name, weight) VALUES (?, ?, ?)",   # add each exercise to db
                       (exercise_id, exercise_name, exercise_weight))
            db.commit()  # commit the exercise insert into the exercises table
        # 2.2 confirm user registration
        print("Registered user " + user_name)
        print("-" * 20)
    else:
        print("User already exists")

# 3. close cursor and db
cursor.close()
db.close()
