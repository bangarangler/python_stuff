import re

def parse_date(input):
  pattern = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
  match = pattern.search(input)
  if match:
    return {
      "d": match.group(1),
      "m": match.group(2),
      "y": match.group(3),
    }
  return None

print(parse_date("06.12.2019"))
print(parse_date("6,12,2019"))
print(parse_date("6/12/20199"))
