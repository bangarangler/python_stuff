# CLASS
#_name internal use in class convention
#__name name mangling / put class name first
#__name__ python specific methods


class User:

  active_users = 0

  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    User.active_users += 1

  # INSTANCE METHOD
  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def initials(self):
    return f"{self.first_name[0]}.{self.last_name[0]}"

  def likes(self, thing):
    return f"{self.first_name} likes {thing}"

  def is_senior(self):
    return self.age >= 65

  def birthday(self):
    self.age += 1
    return f"Happy {self.age}th, {self.first_name}"

  def logout(self):
    User.active_users -= 1
    return f"{self.first_name} has logged out"
user1 = User("jon","dain","jon@test.com",31)
user2 = User('joe',"murph","joe@example.com",65)
# print(user1.first_name, user1.last_name)
# print(user2.first_name, user2.last_name)
print(user1.full_name())
print(user2.full_name())
print(user1.initials())
print(user2.initials())
print(user1.likes("Ice cream"))
print(user2.likes("hibachi"))
print(user2.is_senior())
print(user1.birthday())
print(user1.age)
print(User.active_users)
print(user2.logout())
print(User.active_users)


