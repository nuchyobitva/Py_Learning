sum = 0
a, b = 1, 2
tsd = 4000000
while b<=tsd:
    if b% 2 ==0:
        sum+=b
    a,b = b, a+b
print(sum)
