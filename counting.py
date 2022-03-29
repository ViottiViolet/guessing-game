import random

chances = 0
num = random.randint(1, 9)

guess = int(input("Guess a number from 1 to 9: "))

while chances < 5:
    if guess < num:
        print("Your guess is too low, guess higher than " + str(guess))
    if guess > num:
            print("Your guess is too high, guess lower than " + str(guess))
    if guess == num:
        print("Congrats! You guessed correctly!)
        break

if guess =! num:
    print("You lose! The answer is " + str(num))
