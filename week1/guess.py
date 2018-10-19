#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import random
guess = random.randint(1,10)

attemps = 0
while True:
    user_guess = int(input("Enter a number between [1,10]: "))
    if guess == user_guess:
        print("Congratulations you win!!")
        break
    else:
        attemps+=1
        print("You lose!")
    if attemps == 3:
        print("LOSER")
        break


