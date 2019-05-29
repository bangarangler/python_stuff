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
