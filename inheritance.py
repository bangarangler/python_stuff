class Animal:
  cool = True

  def make_sound(self, sound):
    print(f"this animal says {sound}")

class Cat(Animal):
  pass

blue = Cat()
# blue.make_sound("MEOW")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)

# print(isinstance(blue, object))

class Human:
  def __init__(self,first,last,age):
    self.first = first
    self.last = last
    if age >= 0:
      self._age = age
    else:
      self._age = 0

  # def get_age(self):
    # return self._age

  # def set_age(self, new_age):
    # if new_age >= 0:
      # self._age = new_age
    # else:
      # self._age = 0

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if value >= 0:
      self._age = value
    else:
      raise ValueError("age can not be negative!")

  @property
  def full_name(self):
    return f"{self.first} {self.last}"

  @full_name.setter
  def full_name(self, name):
    self.first , self.last = name.split(' ')

jane = Human("Jane", "Goodall", 34)
# print(jane.get_age())
# print(jane.set_age(45))
# print(jane.get_age())
print(jane.age)
# jane.age = -100
jane.age = 50
print(jane.age)
print(jane.full_name)
jane.full_name = 'Tim Minch'
print(jane.__dict__)

