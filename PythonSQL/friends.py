import sqlite3

conn = sqlite3.connect("my_friends.db")

# create cursor object
c = conn.cursor()

# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
# VALUES ('Merriwether', 'Lewis', 7)'''

# form_first = "Dana"
# DON'T DO THIS
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
# Better way
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first,))
# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"
# people = [
  # ("Roald", "Amundsen", 5),
  # ("Rosa", "Parks", 8),
  # ("Henry", "Hudson", 7),
  # ("Neil", "Armstrong", 7),
  # ("Daniel", "Boone", 3),
# ]
# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
# c.execute(query, data)
# average = 0
# for person in people:
  # c.execute("INSERT INTO friends VALUES (?,?,?)", person)
  # average += person[2]
# print(average/len(people))
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
# for result in c:
  # print(result)
# print(c.fetchone())
print(c.fetchall())
#commit changes
conn.commit()
conn.close()
