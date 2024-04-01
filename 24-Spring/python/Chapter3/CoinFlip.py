import random

# Randomly choose 0 or 1, representing heads or tails
coin = random.randrange(2)

# Initialize the number of attempts
chance = 0

while True:
    # Prompt the user for their guess
    pick = int(input("Guess the coin side (0 for heads, 1 for tails): "))

    # Check if the input is either 0 or 1
    if pick == 0 or pick == 1:
        # Increment the attempt counter
        chance += 1

        # Check if the guess matches the coin toss
        if coin == pick:
            print("Congratulations! You guessed it right.")
            break
        else:
            print("Try again.")
    else:
        print("Please enter 0 or 1 for your guess.")

# Print the total number of attempts
print(f'Your tries: {chance}')
