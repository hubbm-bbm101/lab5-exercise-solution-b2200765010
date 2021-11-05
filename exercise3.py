import numpy as np

random_number = np.random.randint(0, 101)

guess = int(input("Number:"))

while guess != random_number:
    if guess < random_number:
        print("increase your number")

    else:
        print("decrease your number")

    guess = int(input("Number:"))

    if guess == random_number:
        print("You found the number")
