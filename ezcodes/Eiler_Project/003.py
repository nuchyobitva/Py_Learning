from math import sqrt, ceil
def is_prime(n):
    for i in range(2,ceil(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def find_closest_del(n):
    if is_prime(n):
        return n
    for i in range (2,ceil(sqrt(n))+1):
        if n % i == 0:
            return i
    return 1

n = 600851475143
max_del = 1
while n>1:
    x = find_closest_del(n)
    if x > max_del:
        max_del = x
    n //= x
print(max_del)
