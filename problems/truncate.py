'''
shorten a string to a specified lenght, and add "..." to the end. given a
string and a number n, truncate the string to a shorter string containing at
most n characters. ex. "long string", 5 should return a 5 character truncated
version of "long string". if the string gets truncated the truncated return
string should have a "..." at the end. smallest number passed in as a second
argument should be 3
'''

def truncate(string, n):
  if (n < 3):
    return "Truncation must be at least 3 characters."
  if (n > len(string) + 2):
    return string

  return string[:n - 3] + "..."

print(truncate("Hello my name is name!", 5))
print(truncate("This is a really really long senetence for no real reason", 15))
print(truncate("Say what",2))
