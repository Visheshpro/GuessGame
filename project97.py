import random

chances = 3

number = random.randint(0,10)

print("Guess a number between 0 to 10")

guess = int(input("Enter your guess: "))

i = 0

while i < 3:
    if guess > number:
        print("The guess was too high! Try something less than ", guess)
        i +=1
        guess = int(input("Enter your guess: "))
    elif number > guess:
        print("The guess was too low! Try something less than ",guess)
        i += 1
        guess = int(input("Enter your guess: "))
    else:
        print("You won!!")
        break