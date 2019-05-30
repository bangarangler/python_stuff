numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)
print(numbers)

print([num*2 if num % 2 == 0 else num / 2 for num in numbers])

with_vowels = "This is so much fun!"
print(''.join(char for char in with_vowels if char not in 'aeiou'))
