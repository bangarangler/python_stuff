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

names = ['Lassie','Colt','Grump']
print(list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names))))
print([f"Your instructor is {name}" for name in names if len(name) < 5])

def remove_negatives(nums):
  return list(filter(lambda l: l >= 0, nums))

#BUILT-IN FUNCTIONS
# all return True if all elements of iterable are truthy
ppl = ['Charlie','Cody','Carly','Cristina', 'Casey']
print(all([name[0]=='C' for name in ppl]))

#any return true if any element of iterable is truthy
print(any([name[0]]=='Z' for name in ppl))
