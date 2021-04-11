def turn_dig(s):
    tmp = []
    isfir = True
    temnum = 0
    for i in range(len(s)):
        if i > 0:
            isfir = False
        if s[i].isalpha():
            if not isfir:
                tmp.append(temnum)
            if i != len(s) - 1:
                tmp.append(s[i])
            temnum = 0
        else:
            temnum = temnum * 10 + int(s[i])
        if i == len(s) - 1:
            tmp.append(temnum)
    return tmp


inf = open('test.txt', 'r')
s = inf.readline()
s = list(s)
s = turn_dig(s)
for i in range(len(s) // 2):
    print(s[2 * i] * s[2 * i + 1], end = '')
