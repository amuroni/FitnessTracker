import sqlite3
import uuid

db = sqlite3.connect("database.sqlite")
cursor = db.cursor()


def create_database():
    db.execute('CREATE TABLE IF NOT EXISTS users (id TEXT, name TEXT, age INTEGER, weight INTEGER)')
    db.execute('CREATE TABLE IF NOT EXISTS exercises (user_id TEXT, name TEXT, weight INTEGER)')


def create_user(users_num):
    for user in range(0, users_num):
        user_name = input("What's your name")
        cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,))
        if cursor.fetchone() is None:
            user_age = input("What's your age")
            user_weight = input("What's your weight (kg)")
            user_id = str(uuid.uuid1())
            db.execute("INSERT INTO users (id, name, age, weight) VALUES (?, ?, ?, ?)",  # add each user attr to db
                       (user_id, user_name, user_age, user_weight))
            db.commit()
            add_exercise(user_id, user_name)
            print("-" * 20)
            print("Successful registration of user " + user_name)
            print("-" * 20)
        else:
            update_user(user_name)
            print("-" * 20)
            print("Update successful for user " + user_name)
            print("-" * 20)


def update_user(user_name):
    print("User %s already exists" % user_name)
    cursor.execute("SELECT id FROM users WHERE name = ?", (user_name,))
    user_id = cursor.fetchone()[0]
    add_exercise(user_id, user_name)


def add_exercise(user_id, user_name):
    exercise_num = (int(input("Hello %s, how many exercises do you want to track?" % user_name)))
    for exercise in range(0, exercise_num):
        exercise_name = input("What exercise did you do?")
        exercise_weight = input("With how much weight (kg)?")
        exercise_id = user_id
        db.execute("INSERT INTO exercises (user_id, name, weight) VALUES (?, ?, ?)",
                   (exercise_id, exercise_name, exercise_weight))
        db.commit()
        print("-" * 20)
        print("Successfully registered exercise '%s' with %skg weight to user %s"
              % (exercise_name, exercise_weight, user_name))
        print("-" * 20)
