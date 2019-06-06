# CLASS
#_name internal use in class convention
#__name name mangling / put class name first
#__name__ python specific methods


class User:
  active_users = 0

  @classmethod
  def display_active_users(cls):
    return f"There are currently {cls.active_users} active users"

  @classmethod
  def from_string(cls, data_str):
    first, last, email, age = data_str.split(",")
    return cls(first, last, email, int(age))

  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = int(age)
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

  def __repr__(self):
    return f"{self.first_name} is {self.age}"

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
print(User.display_active_users())
tom = User.from_string('Tom,Jones,tom@example.com,77')
print(tom.first_name, tom.email)
print(tom.full_name())
print(tom.birthday())

j = User("judy","steele",'judy@test.com',18)
j = str(j)
print(j)

class Moderator(User):
  total_mods = 0

  def __init__(self,first_name,last_name,email,age,community):
    super().__init__(first_name,last_name,email,age)
    self.community = community
    Moderator.total_mods += 1

  @classmethod
  def display_active_mods(cls):
    return f"There are currently {cls.total_mods} active mods"

  def remove_post(self):
    return f"{self.full_name()} removed a post from the {self.community} community"

jasmine = Moderator("Jasmine", "O'conner", 'jasmine@test.com', 61, "Piano")
u1 = User("Tom","Garcia","tom@example.com",33)
print(u1)
print(jasmine.full_name())
print(jasmine.community)
print(User.display_active_users())
print(Moderator.display_active_mods())
