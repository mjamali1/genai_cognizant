import random
number_to_guess = random.randint(1, 100)
numGuesses = 1

userInput = int(input("Guess the number (between 1 and 100): "))
while userInput != number_to_guess:

    if numGuesses == 10:
        print("Sorry, you've used all your guesses. The number was:", number_to_guess)
        break

    if userInput < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    userInput = int(input("Guess the number (between 1 and 100): "))
    numGuesses += 1
    

print("Congratulations! You've guessed the number.")