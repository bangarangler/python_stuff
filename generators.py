# GENERATORS
'''
generators are iterators. they can be created with geneator functions.
generator functions use the yield keyword and can be created with generator
expressions
function vs generator functions: functions uses return and returns once.
generator functions uses yield and can yield multiple times
function when invoked, returns the return value. generator function when
invoked, returns a generator
'''

def count_up_to(max):
  count = 1
  while count <= max:
    yield count
    count += 1

counter = count_up_to(10)
print(next(counter))
for num in counter:
  print(num)

# BEAT INFINITE GENERATOR
def current_beat():
  nums = (1,2,3,4)
  i = 0
  while True:
    if i >= len(nums): i = 0
    yield nums[i]
    i += 1
