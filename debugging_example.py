# DEUBGGING EXAMPLE

# Import the random module to generate random numbers
import random


def guess_number():
    """
    Starts a guessing game where the user has to guess a random number between 1 and 10.
    
    The function generates a random number, then prompts the user to guess the number.
    The user is given feedback on whether their guess is too high or too low, and the
    number of attempts is tracked. The game continues until the user correctly guesses
    the number, at which point a congratulatory message is printed.
    """
        # Generate a random number between 1 and 10 (inclusive)
    secret = random.randint(1, 10)
    # Initialize the number of attempts to 0
    attempts = 0

    # Start an infinite loop for the guessing game
    while True:
        # Ask the user to input a guess and convert it to an integer
        guess = int(input("Guess a number between 1 and 10: "))
        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret:
            # If correct, print a congratulatory message with the number of attempts
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            # Exit the loop since the correct number was guessed
            break
        elif guess < secret:
            # If the guess is too low, inform the user
            print("Too low. Try again.")
        else:
            # If the guess is too high, inform the user
            print("Too high. Try again.")


# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    # If so, start the guessing game
    guess_number()