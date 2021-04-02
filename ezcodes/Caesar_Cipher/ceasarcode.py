def caesar(sdvig,lang,txt):
    if lang == 'en':
        lft = 97
        length = 26
    elif lang == 'ru':
        lft = 1072
        length = 32
    if sdvig<0:
        sdvig += length
    ans = ''
    for i in txt:
        isup = False
        if i.isupper():
            isup = True
            i = i.lower()
        x = ord(i) % lft
        if not 0<=x<=length-1:
            if isup:
                i = i.upper()
            ans += i
        else:
            i = chr((x+sdvig) % length + lft)
            if isup:
                i = i.upper()
            ans += i
    print(ans,end=' ')


print('Welcome to Caesar Coder/Decoder','\nEnter + if you want to code a text or enter - if you want to Decode a text: ',end = '')
symb = input()
print('Now enter the shift scale:',end=' ')
if symb == '+':
    sdvig = int(input())
elif symb == '-':
    sdvig = -1*int(input())
lang = input('Now enter "en" if the text language is English, or "ru" if it is Russian: ')
txt = input()
caesar(sdvig,lang,txt)
