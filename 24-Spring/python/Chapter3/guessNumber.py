import random

def guessNumber(n):
    guess = random.randint(1, n)
    chance = 0
    while True:
        pick = int(input(f"Guess a number between 1 and {n}: "))
        chance += 1
        if guess > pick:
            print("Up")
            continue
        elif guess < pick:
            print("Down")
            continue
        else:
            print("Congratulations! You're correct!")
            break
    print(f"You tried {chance} times. Answer is {guess}")

range = int(input("Write maximum number: "))
guessNumber(range)