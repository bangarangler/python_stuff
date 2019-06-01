# import random
from random import choice, shuffle
import math
import keyword

print(choice(['apple','banana','cherry','durian']))
print(shuffle(['apple','banana','cherry','durian']))
answer = math.sqrt(15129)
print(answer)

def contains_keyword(*args):
  for item in args:
    if keyword.iskeyword(item): return True
  return False
