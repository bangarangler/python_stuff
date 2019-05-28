# ask for age
age = input('How old are you: ')
if age:
    age = int(age)
    #18-21 wristband
    #if age and (age >= 18 and age < 21)
    if age >= 21:
        print("you are good to enter and can drink!")

  #+21 drink, normal entry
    elif age >= 18:
        print("You can enter, but need a wristband!")
  #too young sorry
    else:
        print("you can't come in, little one! :(")
else:
    print("please enter an age")
