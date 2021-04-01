import random as rnd


def gen_pass(long, chars):
    password = ''
    for _ in range(long):
        password += rnd.choice(chars)
    print(password)


digits = '0123456789'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
count_pass = int(input('How many passwords to generate? '))
long_pass = int(input("Password's length: "))

if input('Type y, if you need lowercase letters: ') == 'y':
    chars += lowercase

if input('Type y, if you need uppercase letters: ') == 'y':
    chars += uppercase

if input('Type y, if you need numbers: ') == 'y':
    chars += digits

if input('Type y, if you need symbols: ') == 'y':
    chars += punctuation

if input('Type y, if you need ambiguous symbols "il1Lo0O": ') != 'y':
    for _ in 'il1Lo0O':
        chars = chars.replace(_, '')

for _ in range(count_pass):
    gen_pass(long_pass, chars)
