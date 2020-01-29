import random


secretnumber = random.randrange(50)

counter = 4

#print(secretnumber)

userguess = int(input("You have four tries to guess the secret number.  Enter a number from 1 to 50 : "))

while userguess != secretnumber:
    counter = counter-1
    if counter == 0:
        print("You lose!")
        break
    if userguess < secretnumber:
        print ("Your guess is too low, try again.")
    else:
        print ("Your guess is too high, try again.")
    userguess = int(input("Enter another guess from 1 to 50 : "))
else:
    print("Congraulations - you guessed the number!")
