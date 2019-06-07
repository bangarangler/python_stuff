def add_positive_numbers(x,y):
  assert x > 0 and y > 0, "Both numbers must be positive!"
  return x + y

print(add_positive_numbers(1,1)) # 2
# print(add_positive_numbers(1,-1)) # AssertionError:

def eat_junk(food):
  assert food in ['pizze','ice cream', 'candy','fried butter'], 'food must be a junk food'
  return f"Nom Nom I am eating {food}"

food = input('enter a food please: ')
print(eat_junk(food))
