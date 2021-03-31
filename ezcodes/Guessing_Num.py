from math import ceil, log2, floor
import random


def isnt_valid(n, x):
    if x > n or x < 1:
        print('Кажется, вы ввели число вне данного диапазона', end='')
        print(', давайте играть по правилам :)')
        return True
    if floor(x) != ceil(x):
        print('Кажется, вы ввели нецелое число', end='')
        print(', давайте играть по правилам :)')
        return True
    return False


def is_right(guess, x):
    if guess == x:
        print('Поздравляю, вы угадали! Вашей интуиции можно позавидовать :)')
        return True
    else:
        print('Неверно, попробуйте ещё раз!', 'Загаданное число', end='')
        if guess > x:
            print(' больше введённого')
        elif guess < x:
            print(' меньше введённого')
    return False


def game():
    print('Сегодня у вас будет возможность угадать число в диапазоне от 1 до n',
          'Для этого введите n:', sep='\n', end=' ')
    n = int(input())
    result = 0
    guess = random.randint(1, n)
    x = -1
    while x != guess:
        print('Мы загадали число! Угадывайте, оно в промежутке от 1 до', n)
        x = int(input('Вводите число: '))
        result += 1
        if isnt_valid(n, x):
            result -= 1
        if is_right(guess, x):
            break
    print('Ваш результат -', result)
    print('Минимальное количество попыток -', ceil(log2(n)))
    if result <= ceil(log2(n)):
        print('Вы показали лучший результат!')


print('Добрый день! Добро пожаловать в угадайку чисел!')
play = 'да'
while play == 'да':
    game()
    play = input('Введите "да", если хотите поиграть ещё раз или другой текст, если хотите выйти: ')
print('Спасибо за игру и удачи!')
