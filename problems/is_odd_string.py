'''
returns true if sum of each character's position in the alphabet is odd. ex.
"a" is in the first position, "b" is in the second position, and so on. if sum
is even, return false. NOTE: indexing starts at 1. A is position 1, not
position 0.
'''

def is_odd_string(string):
  total = sum((ord(c) - 96) for c in string.lower()) or 0
  return total % 2 == 1

print(is_odd_string('abcdefg'))
