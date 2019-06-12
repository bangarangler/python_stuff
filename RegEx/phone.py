import re

def extract_phone(input):
  phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
  match = phone_regex.search(input)
  if match:
    return match.group()
  return None

def extract_all_phones(input):
  phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
  return phone_regex.findall(input)

# print(extract_phone("my number is 353 484-5867"))
# print(extract_phone("my number is 949 839-826588"))
# print(extract_phone("739 938-2634 asdfasdffdsa"))
# print(extract_phone("739 938-2634"))
# print(extract_all_phones("my number is 938 847-3745 or call me at 232 989-2938"))
# print(extract_all_phones("my number is 938 8"))

# def is_valid_phone(input):
  # phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
  # match = phone_regex.search(input)
  # if match:
    # return True
  # return False

def is_valid_phone(input):
  phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
  match = phone_regex.fullmatch(input)
  if match:
    return True
  return False

print(is_valid_phone('393 945-3928'))
print(is_valid_phone('393 945-3928 asdffa'))
print(is_valid_phone('asklj 393 945-3928 d'))
