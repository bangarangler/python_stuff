import sqlite3

conn = sqlite3.connect("users.db")

query = "CREATE TABLE users (username TEXT, password TEXT)"

u = input("please enter you username...")
p = input("please enter you password...")
# don't do this
# query = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
# better option
# query = f"SELECT * FROM users WHERE username=? AND password=?"
# "SELECT * FROM users WHERE username='' AND password = ''"

c = conn.cursor()
c.execute(query)
# c.execute(query,(u,p))

result = c.fetchone()
if(result):
  print("welcome back")
else:
  print("failed login")

conn.commit()
conn.close()
