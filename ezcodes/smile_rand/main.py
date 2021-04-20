import random
n = 100  #  the number of smiles needed to be generated
s = '💞💓😍🥰❤😘😻💕💗'
s = list(s)
for _ in range(n):
    print(s[random.randint(0,8)],end='')
