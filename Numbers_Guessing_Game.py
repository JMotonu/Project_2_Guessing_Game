import random


def save_score(username, score):
    with open("scores.txt", "a") as file:
        file.write(f"{username} - {score}\n")


def get_hint(number):
    if number % 2 == 0:
        return "Hint: The number is even."
    else:
        return "Hint: The number is odd."


print("===================================")
print("      NUMBER GUESSING GAME")
print("===================================")

username = input("Enter your name: ")

print("\nChoose Difficulty")
print("1. Easy (10 tries)")
print("2. Medium (7 tries)")
print("3. Hard (5 tries)")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    attempts = 10
elif choice == "2":
    attempts = 7
elif choice == "3":
    attempts = 5
else:
    print("Invalid choice. Defaulting to Easy.")
    attempts = 10

secret_number = random.randint(1, 100)

remaining = attempts
wrong_guesses = 0

while remaining > 0:

    try:
        guess = int(input("\nGuess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret_number:
        print("\n🎉 Congratulations!")
        print(f"You guessed the number in {attempts - remaining + 1} attempts.")
        
        score = remaining
        save_score(username, score)

        print(f"Score saved! Score: {score}")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

    wrong_guesses += 1
    remaining -= 1

    print(f"Remaining guesses: {remaining}")

    if wrong_guesses == 3:
        print(get_hint(secret_number))

else:
    print("\nGame Over!")
    print(f"The number was {secret_number}.")