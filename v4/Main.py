from v4.Database import *

# 1.create databases for users and exercises
Database = Database()
Database.create_database()
# 2. ask user input for n. of users to create
users_num = int(input("How many users would you like to create/update?"))
Database.create_user(users_num)
# 3. close cursor and db
Database.cursor.close()
Database.db.close()
