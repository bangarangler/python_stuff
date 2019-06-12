import re

'''
time must start with a digit, and there can be a second optional digit
before the colon. Then there's the colon and two mandatory digits.
'''

def is_valid_time(input):
  pattern = re.compile(r"^\d\d?:\d\d$")
  match = pattern.search(input)
  if match:
    return True
  return False

print(is_valid_time("4:00"))
print(is_valid_time("12:35"))
print(is_valid_time("120:35"))
print(is_valid_time("12:359"))
print(is_valid_time("time"))
