def vowel_count(string):
  '''accepts a string and returns a dictionary with the keys as the vowels and
  values as the count of times vowel appeard in the string'''
  lower_s = string.lower()
  return {letter: lower_s.count(letter) for letter in lower_s if letter in 'aeiou'}

print(vowel_count("what is your name? Where do you come from?"))
