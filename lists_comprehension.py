numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)
print(numbers)

print([num*2 if num % 2 == 0 else num / 2 for num in numbers])

with_vowels = "This is so much fun!"
print(''.join(char for char in with_vowels if char not in 'aeiou'))

# Nested Lists
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in nested_list:
  for val in i:
    print(val)

[[print(val) for val in i] for i in nested_list]

coords = [[10.423,9.132],[37.212,-14.092],[21.367,32.572]]
for loc in coords:
  for coord in loc:
    print(coord)

print(['*' for i in range(1,4)])

print([['*' for x in range(1,4)] for i in range(1,4)])
