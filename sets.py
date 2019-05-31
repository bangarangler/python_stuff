# SETS

a = {1,4,5}

print(4 in a)

for stuff in a:
  print(stuff)

a.add(6)
a.remove(6)
a.discard(8)
b = a.copy()
b.clear()
print(b)
print(a)

#SET COMPREHENSION
print({x**2 for x in range(10)})

string = 'sequoia'
print(len({char for char in string if char in 'aeiou'}) == 5)
