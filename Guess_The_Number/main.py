import random

print("     Hello, let's begin the guessing game \n\n")

numberoftries = 0
minn = 1
maxx = 10
number = random.randint(minn , maxx)

print(f"     Take any guess between {minn} and { maxx }")

while numberoftries < 3:
    print(f"     Try: {numberoftries}")
    guess = input()
    guess = int(guess)

    numberoftries = numberoftries + 1

    if guess < (number):
        print("     your guess is too low")

    if guess > (number):
        print("     Your guess is too high")

    if guess == number:
        break

if guess == number:
    print("     Congratulations, you have won 1 trillion billion million dollars")
    print('     .\n')

if guess != number:
    print("     Sorry, better luck next time")
    print("     .\n")
    


