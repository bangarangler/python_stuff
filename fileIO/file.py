# with open("example.txt", 'r+') as file:
  # file.write(": )\n")
  # file.seek(10)
  # file.write(": (")

# def copy(file_name, new_file_name):
  # with open(file_name) as file:
    # text = file.read()

  # with open(new_file_name, "w") as new_file:
    # new_file.write(text)

# copy('example.txt', 'example_copy.txt')

# def copy_and_reverse(file_name, new_file_name):
  # with open(file_name) as file:
    # text = file.read()

  # with open(new_file_name, "w") as new_file:
    # new_file.write(text[:: -1])

# copy_and_reverse("example.txt", "reverse_example.txt")

# '''
# statistics('example.txt')
# # {'lines': 172, 'words': 2134, 'characters': 11445}
# '''
# def statistics(file_name):
  # with open(file_name) as file:
    # lines = file.readlines()

  # return { "lines": len(lines),
            # "words": sum(len(line.split(" ")) for line in lines),
            # "characters": sum(len(line) for line in lines)
          # }

# print(statistics("example.txt"))

def find_and_replace(file_name, old_word, new_word):
  with open(file_name, "r+") as file:
    text = file.read()
    new_text = text.replace(old_word, new_word)
    file.seek(0)
    file.write(new_text)
    file.truncate()

find_and_replace("example.txt","one","two")
