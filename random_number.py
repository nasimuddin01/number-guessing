# Guess the number game

import random

randomnumber = random.randint(1,50)

totalcount = 6
counter = 1

while counter <= totalcount:
    print("Remaining guesses:",(totalcount - counter))
    inputnumber = int(input("Input your guess:\n"))

    if inputnumber == randomnumber:
        print("Your guess is correct!!")
        break;
    elif inputnumber < randomnumber:
        if counter == totalcount:
            print("\nYou loose stupid!")
            break
        else:
            print("Your guess number is too low")
    else:
        if counter == totalcount:
            print("\nYou loose stupid!")
            break
        else:
            print("Your guess number is too high")

    counter += 1
else:
    print("\nYou loose stupid!")
