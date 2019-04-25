from v4.Database import *

# 1.create databases object with tables: users and exercises
Database = Database()
Database.create_database()
# 2. create/update users and register exercises
Database.create_user()
# 3. close Database cursor and db
Database.cursor.close()
Database.db.close()
