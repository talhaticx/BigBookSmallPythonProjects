import random

DIGIT_LEN = 3
GUESSES = 10

def printHints():
    print("WELCOME TO THE GAME")
    print(
"""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:

Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.

I have thought up a number.
    You have 10 guesses to get it.\n"""
)
    
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.


    secretNum = ''
    for i in range(DIGIT_LEN):
        secretNum += str(numbers[i])
    return secretNum

def evalGuess(guess, num):
    clue = []
    for i in range(DIGIT_LEN):
        if guess[i] in num:
            if guess[i] == num[i]:
                clue.append("Fermi")
            else:
                clue.append("Pico")
    
    return clue        

def game():
    printHints()
    secretNum = getSecretNum()
    
    for i in range(1, GUESSES+1):
        print(f"Guess No. {i}\n")
        print("Enter: ", end="")
        while True:
            guess = input()
            try:
                if len(guess) != 3:
                    raise ValueError
                check = int(guess)
                break
            except:
                print("\nEnter Again: ", end="")
                continue
        
        clues = evalGuess(str(guess), secretNum)
        
        if len(clues) == 0:
            print("bagels")
        if len(clues) == 3:
            print("You Got it")
            break
        for clue in clues:
            print(clue)
        
        print()      
        
        
        
if __name__ == "__main__":
    while True:
        game()
        choice = input("Wanna Play Again (y or n): ")
        print()
        if choice == "y":
            continue
        else:
            break