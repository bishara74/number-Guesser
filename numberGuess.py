import random

number = random.randint(1, 100)

num_guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    num_guesses += 1
    if guess == number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
