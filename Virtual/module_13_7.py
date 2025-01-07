import sqlite3
import random

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser", "ex@gmail.com", "28")  )
# cursor.execute("DELETE  FROM Users")

# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", \
#                    (f"newuser{i}", f"ex{i}@gmail.com", str(random.randint(20, 60)))  )

# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser")  )
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",)  )
# cursor.execute("SELECT * FROM users")

cursor.execute("SELECT username, age FROM users WHERE age > 40")
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
