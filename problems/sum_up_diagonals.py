'''
accepts an NxN list of lists and sums the two main diagonals in array. one from
upper left to lower right, and one from upper right to lower left.
list1 = [[1,2], [3,4]]
'''

def sum_up_diagonals(arr):
  total = 0

  for i, val in enumerate(arr):
    total += arr[i][i]
    total += arr[i][-1-i]

  return total

print(sum_up_diagonals(([1,2],[3,4])))
