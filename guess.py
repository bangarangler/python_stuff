from random import randint

computer_guess = randint(1,10)
# player_guess = None

while True:
  player_guess = input("Pick a number from 1 to 10: ")
  player_guess = int(player_guess)
  if player_guess < computer_guess:
    print("TOO LOW")
  elif player_guess > computer_guess:
    print("TOO HIGH")
  else:
    print("YOU WON!!!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'y':
      computer_guess = randint(1,10)
      player_guess = None
    else:
      print("Thanks for playing!")
      break

print(computer_guess)
