import random
#/Users/donjoseph/Documents/Projects/guessing game/guessing-game.py


print("Welcome to guess the number. The computer will generate a random number between 1 and 1000. You win when you guess the number")


def guess(x):
    randint = random.randint(1,x)
    guess = 0
    while guess != randint:
        guess = int(input("Guess a number: "))
    print("You Win!")


guess(10)