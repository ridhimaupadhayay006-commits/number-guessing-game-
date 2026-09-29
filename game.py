import random


def show_welcome():
    print("=" * 50)
    print("       NUMBER GUESSING GAME")
    print("=" * 50)
    print("Try to guess the number I'm thinking of!")
    print("I'll tell you if your guess is too high or too low.\n")


def difficulty():
    print("Choose a difficulty:")
    print("1. Easy   - 1 to 50   (10 chances)")
    print("2. Medium - 1 to 100  (7 chances)")
    print("3. Hard   - 1 to 200  (5 chances)")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 5
        else:
            print("Please enter 1, 2 or 3.")


def game():
    low, high, chances = difficulty()

    number = random.randint(low, high)
    tries = 0

    print(f"\nI have picked a number between {low} and {high}.")
    print(f"You have {chances} chances to guess it.\n")

    while tries < chances:
        guess = input(f"Enter your guess ({tries + 1}/{chances}): ")

        if not guess.isdigit():
            print("Please enter a number.\n")
            continue

        guess = int(guess)

        if guess < low or guess > high:
            print(f"Your number should be between {low} and {high}.\n")
            continue

        tries += 1

        if guess == number:
            score = (chances - tries + 1) * 10

            print("\nYou got it!")
            print("The number was:", number)
            print("You took", tries, "tries.")
            print("Your score is:", score)
            return score

        if guess < number:
            print("Too low!")
        else:
            print("Too high!")

        print("Chances left:", chances - tries)
        print()

    print("\nGame over!")
    print("The number was:", number)
    return 0


def main():
    show_welcome()

    high_score = 0

    while True:
        score = game()

        if score > high_score:
            high_score = score
            print("New high score:", high_score)

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes" and again != "y":
            print("\nThanks for playing!")
            print("Your high score was:", high_score)
            break


main()