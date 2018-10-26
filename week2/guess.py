import random

number = random.randint(1,10)
#print("The random number is:")
#print(number)
#print(user_guess)
lives = 3
while True:
    if lives <= 0:
        print("Game over!")
        break
    user_guess = input()
    if number == int(user_guess):
        print("Success!")
        break
    else:
        print("you're wrong")
        lives = lives - 1


