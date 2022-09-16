import random
def computer_guesses(x):
    counter = 1
    user_num = int(input("Enter a number between 1 and 10 inclusive: "))
    randint = random.randint(1,x)
    while user_num != randint:
        randint = random.randint(1,x)
        print(f"The computer guesses {randint}")
        if randint != user_num:
            print("The computer guessed wrong! It will try again")
            counter = counter + 1
        
    print(f"Computer guesses {randint} and your number was {user_num}. GAME OVER!")
    print(f"It took the computer {str(counter)} tries.")

computer_guesses(10)