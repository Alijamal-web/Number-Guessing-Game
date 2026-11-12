import random

secret_number = random.randint(1, 20)
print("I have guessed a number from 1 to 20. You have 5 attempts to guess it!")

for attempt in range(1, 6):
    guess = int(input("Attempt : Enter number → "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("My number is larger.")
    else:
        print("My number is smaller.")
else:
    print("You have run out of attempts. The number you were given was: {secret_number}")
