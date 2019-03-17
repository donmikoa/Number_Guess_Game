import random

number = random.randint(1, 10)
tries = 1

user_name = input("Hi, What is your username")

print("Hi", user_name + ".",)

question = input("Would you like to play a game? [Y/N]")
if question == "n":
    print("Have a nice day")


if question == "y":
    print("I'm thinking of a number between 1 and 10")
    guess = int(input("Guess the number:"))
    if guess > number:
        print("Guess Lower...")

if guess < number:
        print("Guess Higher...")
while guess != number:
    tries += 1
    guess = int(input("Try again..."))
if guess == number:
    print("You win, the number was", number,







