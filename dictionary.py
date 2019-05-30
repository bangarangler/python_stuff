# DICTIONARIES
instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num-courses": 4,
  "favorite_language": "Python",
  "is_hillarious": False,
  44: "my favorite number!"
}

print(instructor["name"])

cat = {
  "name": "Molly",
  "age": 3.5,
  "is_cute": True
}
print(cat)

cat2 = dict(name="murph", age=.5)
print(cat2)

person = {
  "name": "Jon",
  "age": 31,
  "is_learning": True
}

print(person['is_learning'])
print(person["name"])
age = "age"
print(person[age])

print(instructor.values())
for value in instructor.values():
  print(value)

print(instructor.keys())
for v in instructor.keys():
  print(v)

print(instructor.items())

for key,value in instructor.items():
  print(f"key is: {key}, value is {value}")

print("name" in instructor)
print("phone" in instructor)

if "phone" in instructor:
  print( 'There is a phone!')
else:
  print("sorry no phone")

# CLEAR .clear() empties out dictionary
# COPY .copy() makes a copy of dictionary
# FROMKEYS {}.fromkeys("a","b") === {'a': 'b'}

new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user)

# GET retrieves a key in an object and return None
print(instructor.get('name'))
print(cat.get('phone'))

