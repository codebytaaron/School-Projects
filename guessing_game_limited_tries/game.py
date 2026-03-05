import 

print("Welcome to the Guessing Game!")

secret = random.randint(1, 20)

tries = 0
max_tries = 5

print("I am thinking of a number from 1 to 20.")
print("You have 5 tries.")

while tries < max_tries:

    guess = int(input("Enter your guess: "))
    tries = tries + 1

    if guess == secret:
        print("You win!")
        break
    elif guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

# Small mistake on purpose
if tries == max_tries:
    print("You ran out of tries.")
    print("The number was", guess)
