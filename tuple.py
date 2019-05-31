alphabet = ('a','b','c','d')

months = ('January','February','March','April','May','June','July','August','September','October','November','December')

for month in months:
  print(month)

i = len(months) -1
while i >= 0:
  print(months[i])
  i -= 1

print(months.count('March'))
print(months.index('March'))
