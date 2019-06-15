'''
accepts a list of numbers and returns True if any three consecutive numbers sum
to an odd number
'''

def three_odd_numbers(arr):
  i = 0
  while(i < (len(arr) -2)):
    total = 0
    j = i
    while(j <= i + 2):
      total += arr[j]
      j += 1

    if (j-i) % 3 == 0 and total % 2 != 0:
      return True

    i += 1
  return False

print(three_odd_numbers([3,5,7,9]))
