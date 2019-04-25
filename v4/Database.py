import sqlite3
import uuid


class Database:

    def __init__(self):
        self.db = sqlite3.connect("database.sqlite")
        self.cursor = self.db.cursor()

    def create_database(self):
        self.db.execute('CREATE TABLE IF NOT EXISTS users (id TEXT, name TEXT, age INTEGER, weight INTEGER)')
        self.db.execute('CREATE TABLE IF NOT EXISTS exercises (user_id TEXT, name TEXT, weight INTEGER)')

    def create_user(self, users_num):
        for user in range(0, users_num):
            user_name = input("What's your name")
            self.cursor.execute("SELECT * FROM users WHERE name = ?", (user_name,))
            if self.cursor.fetchone() is None:
                user_age = input("What's your age")
                user_weight = input("What's your weight (kg)")
                user_id = str(uuid.uuid1())
                self.db.execute("INSERT INTO users (id, name, age, weight) VALUES (?, ?, ?, ?)",
                                (user_id, user_name, user_age, user_weight))
                self.db.commit()
                self.add_exercise(user_id, user_name)
                print("-" * 20)
                print("Successful registration of user " + user_name)
                print("-" * 20)
            else:
                self.update_user(user_name)
                print("-" * 20)
                print("Update successful for user " + user_name)
                print("-" * 20)

    def update_user(self, user_name):
        print("User %s already exists" % user_name)
        self.cursor.execute("SELECT id FROM users WHERE name = ?", (user_name,))
        user_id = self.cursor.fetchone()[0]
        self.add_exercise(user_id, user_name)

    def add_exercise(self, user_id, user_name):
        exercise_num = (int(input("Hello %s, how many exercises do you want to track?" % user_name)))
        for exercise in range(0, exercise_num):
            exercise_name = input("What exercise did you do?")
            exercise_weight = input("With how much weight (kg)?")
            exercise_id = user_id
            self.db.execute("INSERT INTO exercises (user_id, name, weight) VALUES (?, ?, ?)",
                            (exercise_id, exercise_name, exercise_weight))
            self.db.commit()
            print("-" * 20)
            print("Successfully registered exercise '%s' with %skg weight to user %s"
                  % (exercise_name, exercise_weight, user_name))
            print("-" * 20)
