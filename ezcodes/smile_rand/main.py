import random
bln = [True, False]
pch = ''
ft = ''
if not random.choice(bln):
    pch, ft = ft, pch
s = '❤💞💓😍🥰😘😻💕💗' 
s = list(s)
for i in range(random.randint(270,330)):
    print(s[random.randint(0,8)],end='')
    if i == 100:
        print(pch,end='')
    elif i == 200:
        print(ft, end = '')
print(s[0])
