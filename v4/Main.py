from v4.Database import *

# 1.create databases for users and exercises
create_database()
# 2. ask user input for n. of users to create
users_num = int(input("How many users would you like to create?"))
add_user(users_num)
# 3. close cursor and db
cursor.close()
db.close()
