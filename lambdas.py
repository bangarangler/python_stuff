#LAMBDAS

def square(num): return num * num

print(square(9))

square2 = lambda num: num * num
print(square2(7))

add = lambda a,b: a+b
print(add(3,4))

cube = lambda num: num **3

nums = [2,3,6,9,3]
doubles = map(lambda x: x*2, nums)
print(list(doubles))

people = ['Darcy','Christina', "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
print(list(peeps))

def double(x): return x*2
print(double(3))

def decrement_list(l):
  return list(map(lambda n: n-1, l))

#FILTER
l = [1,2,3,4]
evens = list(filter(lambda x: x%2 == 0, l))
print(evens)

names = ['abby','autumn','arthur','brady']
a_names = filter(lambda n: n[0]=='a', names)
print(list(a_names))
