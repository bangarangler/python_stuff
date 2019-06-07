# POLYMORPHISM
'''
principal in OOP. an abject can take on many (poly) forms (morph)
1. the same class method works in a similar way for different classes
method in a base (or parent) class that is overridden by a subclass ... method
overriding.
each subclass will have a different implementaition of the method
2. same operation works for different kinds of objects
'''
'''
String Representation Example
__repr__ method is one of several ways to provide a nicer string
representation
'''
from copy import copy
class Animal():
  def speak(self):
    return NotImplementedError("Subclass needs to implement method")

class Dog(Animal):
  def speak(self):
    return "woof"

class Cat(Animal):
  def speak(self):
    return "meow"

class Fish(Animal):
  pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())

class Human:
  def __init__(self,first,last,age):
    self.first = first
    self.last = last
    self.age = age
  def __repr__(self):
    return f"Human named {self.first} {self.last} age {self.age}"

  def __len__(self):
    return self.age

  def __add__(self,other):
    if isinstance(other,Human):
      return Human(first="Newborn",last=self.last,age=0)
    return "You can't add that!"

  def __mul__(self,other):
    if isinstance(other, int):
      return [copy(self) for i in range(other)]
    return "can't multiply!"

j = Human('Jenny','Larsen',47)
k = Human('Keven','Jones',49)
print(j)
print(len(j))

print(j + k)
# triplets = j * 3
# triplets[1].first = 'Jessica'
# print(triplets)

triplets = (k + j) * 3
print(triplets)
