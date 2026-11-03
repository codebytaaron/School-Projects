import random

# Pick a random number
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number from 1 to 10.")

guess = 0
tries = 0

# Keep asking until correct
while guess != secret_number:
    
    guess = int(input("Enter your guess: "))
    tries = tries + 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Correct!")
        print("You guessed it in", tries, "tries.")

print("Thanks for playing!")
