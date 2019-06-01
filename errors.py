# try except else finally
while True:
  try:
    num = int(input('please enter a number: '))
  except ValueError:
    print('thats not a number')
  else:
    print('Good job, thats a number')
    break
  finally:
    print('runs no matter what')
print('rest of logic here')
