import re

# pat = re.compile(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')

pattern = re.compile(r"""
  ^([a-z0-9_\.-]+)    # first section of email
  @                   # single @ sign
  ([\da-z\.-]+)       # email provider
  \.                  # single period
  ([a-z\.]{2,6})$     # com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)

match = pattern.search("Timmy123@YahOO.com")
print(match.group())
print(match.groups())


