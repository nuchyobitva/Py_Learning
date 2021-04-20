import random
s = '💞💓😍🥰❤😘😻💕💗'
s = list(s)
for _ in range(100):
    print(s[random.randint(0,8)],end='')
