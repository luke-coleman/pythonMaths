import random

randomNumber = random.randint(1, 100)
guess = 0
guessesNeeded = 0

while guess != randomNumber:
    guess = int(input("Take your best guess:"))
    guessesNeeded = guessesNeeded+1

    if guess == randomNumber:
        print("Nice one! You got the number!")
    elif guess < randomNumber:
        print("Try again! Try going higher!")
    else:
        print("Try again! Try going lower!")