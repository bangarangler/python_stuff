# POLYMORPHISM
'''
principal in OOP. an abject can take on many (poly) forms (morph)
1. the same class method works in a similar way for different classes
method in a base (or parent) class that is overridden by a subclass ... method
overriding.
each subclass will have a different implementaition of the method
2. same operation works for different kinds of objects
'''

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
