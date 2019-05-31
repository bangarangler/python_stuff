# DICTIONARY COMPREHENSIONS
student = {
  "name": "jon",
  "city": "gastonia",
  'color': 'green'
}

yelling_student = {k.upper():v.upper() for k,v in student.items()}
print(yelling_student)

num_list = [1,2,3,4]
print({ num: ("even" if num % 2 == 0 else "odd") for num in num_list })

