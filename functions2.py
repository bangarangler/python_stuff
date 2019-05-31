#FUNCTIONS 2
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  return total

print(sum_all_nums(2,4,5,8,67))

def contains_purple(*args):
  if "purple" in args: return True
  return False

def fav_colors(**kwargs):
  for person, color in kwargs.items():
    print(f"{person}'s favorite color is {color}'")
fav_colors(colt='purple',ruby='red',ethel='teal')

def special_greeting(**kwargs):
  if "Matt" in kwargs and kwargs["Matt"] == "special":
    return "You get a special greeting Matt!"
  elif "Matt" in kwargs:
    return f"{kwargs['Matt']} Matt!"
  return "Not sure who this is..."

print(special_greeting(Matt="Hello"))
print(special_greeting(Linz="Hello"))
print(special_greeting(Matt="special"))
