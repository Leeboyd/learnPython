import math
print('Please think of a number between 0 and 100!')

i = 1
n = 100
guess = n
userInput = ''
guess = math.floor(guess - (n/ (2 ** i)))
# print('Is your secret number ' + str(guess) + '?')
# userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while userInput != 'c':
    # i += 1
    # guess = guess + sign * (n/ (2 ** i))
    print('Is your secret number ' + str(guess) + '?')
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (userInput == 'l'):
        i += 1
        guess = math.floor(guess + (n/ (2 ** i)))
    elif (userInput == 'h'):
        i += 1
        guess = math.floor(guess - (n/ (2 ** i)))
    elif (userInput == 'c'):
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(guess))