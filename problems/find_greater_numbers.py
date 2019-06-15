'''
accepts a list and returns the number of times a number is followed by a larger
number across the entire list.
find_greater_numbers([6,1,2,7]) -> # 4
'''

def find_greater_numbers(arr):
  count = 0
  i = 0
  j = 1
  while i < len(arr):
    while j < len(arr):
      if arr[j] > arr[i]:
        count += 1
      j += 1
    j = i + 1
    i += 1
  return count

print(find_greater_numbers([6,1,2,7]))
