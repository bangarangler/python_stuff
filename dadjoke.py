import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("DAD JOKE!")
header = colored(header, color="blue")
print(header)

while True:
    user_input = input("What would you like to search for? q or quit to exit  ")
    if user_input == "q" or user_input == "quit":
      break
    else:
      url = "https://icanhazdadjoke.com/search"
      res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": user_input}
      ).json()
# json_res = res.json()
      num_jokes = res['total_jokes']
      results = res['results']
      if num_jokes > 1:
        print(f"many jokes: {num_jokes} to be specific... here's one about {user_input}")
        print(choice(results)['joke'])
      elif num_jokes == 1:
        print(f"we have one joke about {user_input}")
        print(results[0]['joke'])
      else:
        print(f"sorry no jokes for: {user_input}")
      print(len(res["results"]))

