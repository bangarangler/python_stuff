# import pdb
first = "First"
second = "Second"
# pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

#l,n,c, type vars to see values l list, n next, c continue

def add_numbers(a,b,c,d):
  import pdb; pdb.set_trace()

  return a + b + c + d
add_numbers(1,2,3,4)

def divide(a,b):
  try:
    total = a / b
  except TypeError:
    return "Please provide two integers or floats"
  except ZeroDivisionError:
    return 'Please do not divide by zero'
  return total


