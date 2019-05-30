# LISTS

cart = []

while True:
  new_item = input('Add something to the cart? q to quit: ')
  new_item = str(new_item)

  if new_item == 'quit' or new_item == 'q':
    print('goodbye')
    break

  else:
    cart.append(new_item)
    for itm in cart:
      print(itm)

# LIST COMPREHENSION
numbers = [1,2,3,4,5]
doubled_numbers = []
for num in numbers:
  doubled_number = num * 2
  doubled_numbers.append(doubled_number)
print(doubled_numbers)

doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

name = 'magic'
print([char.upper() for char in name])

friends = ['ashley', 'matt', 'jeff']
print([friend[0].upper() + friend[1:] for friend in friends])
print([friend.capitalize() for friend in friends])
print(friends)

print([num * 10 for num in range(1,6)])
print([bool(val) for val in [0,[], ""]])

numz = [1,2,3,4,5]
string_list = [str(num) for num in numz]
print(string_list)

colors = ['red','orange','yellow','green','blue','indigo','violet']
print([color.upper() for color in colors])
