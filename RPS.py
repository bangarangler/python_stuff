from random import randint

print("Rock")
print("Paper")
print("Scissors")

player = input("Player, make your move: ").lower()

rand_num = randint(0,2)
if rand_num == 0:
  computer = 'rock'
elif rand_num == 1:
  computer = 'paper'
else:
  computer = 'scissors'
print(f'computer plays {computer}')



if player == computer:
  print('It\'s a tie!')

elif player == 'rock':
  if computer == 'scissors':
    print('player wins')
  else:
    print('computer wins1')

elif player == 'paper':
  if computer == "scissors":
    print('computer wins!')
  elif computer == 'rock':
    print('player wins!')

elif player == 'scissors':
  if computer == "paper":
    print('player wins!')
  elif computer == 'rock':
    print('computer wins!')

else:
  print("Please enter a valid move")


