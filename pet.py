class Pet:

  # CLASS ATTRIBUTE
  allowed = ['cat','dog','fish','rat','pig','bird']

  def __init__(self, name, species):
    if species not in Pet.allowed:
      raise ValueError(f"You can't have a {species} pet!")
    self.name = name
    self.species = species

  def set_species(self, species):
    if species not in Pet.allowed:
      raise ValueError(f"You can't have a {species} pet!")
    self.species = species

cat = Pet("Blue", "cat")
dog = Pet('Wyatt', 'dog')
