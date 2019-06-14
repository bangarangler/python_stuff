def sum_pairs(ints, s):
  '''accepts a list and a number and returns the first pair of numbers that sum
  to the number passed into the function'''
  already_visited = set()
  for i in ints:
    difference = s - i
    if difference in already_visited:
      return [difference, i]
    already_visited.add(i)
  return []

print(sum_pairs((2,4,3,5,10),8))
