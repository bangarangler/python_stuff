numbers = [1,2,3,4]
colors = ["purple","teal","orange","magenta","crimson","emerald"]
i = 0

for color in colors:
  print(color)

# while i < len(numbers):
  # print(numbers[i])
  # i += 1

while i < len(colors):
  print(f"{i}: {colors[i]}")
  i += 1

sounds = ['super','cali','fragil','istic','expi','ali','docious']

result = ''
for s in sounds:
  result += s.upper()
# result = result.upper()
print(result)
