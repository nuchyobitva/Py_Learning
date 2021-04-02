from math import ceil, log2, floor
import random


def isnt_valid(n, x):
    if floor(x) != ceil(x):
        print('Is seems the entered number is not integer', end='')
        print(", let's play by rules :)")
        return True
    if x > n or x < 1:
        print('The entered number is out of range', end='')
        print(", let's play by rules :)")
        return True
    return False


def is_right(guess, x):
    if guess == x:
        print('Congratulations, you won! Your intuition is enviable :)')
        return True
    else:
        print('Wrong, try again!', 'The hidden number', end='')
        if guess > x:
            print(' is greater')
        elif guess < x:
            print(' is lower')
    return False


def game():
    print("Today you'll have an opportunity to guess a number in 1 to n range",
          'To start the game enter "n":', sep='\n', end=' ')
    n = int(input())
    result = 0
    guess = random.randint(1, n)
    x = -1
    while x != guess:
        print("We chose the number! Guess it, it's in the range from 1 to", n)
        x = float(input('Enter the number: '))
        result += 1
        if isnt_valid(n, x):
            result -= 1
            continue
        if is_right(guess, x):
            break
    print('Your result is -', result)
    print('Minimal entries to guess -', ceil(log2(n)))
    if result <= ceil(log2(n)):
        print('Your result is the best!')


print('Hello! Welcome to the Guess the Number Game!')
play = 'yes'
while play == 'yes':
    game()
    play = input('Enter "yes", if you want to play again, or other text if you want to leave: ')
print('Thanks for the good game!')
