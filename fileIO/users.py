import csv

def add_user(first_name, last_name):
  with open("users.csv", 'a') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([first_name, last_name])

def print_users():
  with open("users.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
      print("{} {}".format(row['First Name'], row['Last Name']))

def find_user(first_name, last_name):
  with open("users.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for (index, row) in enumerate(csv_reader):
      first_name_match = first_name == row[0]
      last_name_match = last_name == row[1]
      if first_name_match = last_name_match:
        return index
    return "{} {} not found.".format(first_name, last_name)


add_user("Mike", "Frost")

