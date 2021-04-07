def is_palindrom(x):
    s = str(x)
    n = len(s)
    if n<2:
        return True
    if n%2==0:
        n //= 2
        return s[0:n] == s[n*2:n-1:-1]
    else:
        n = (n-1)//2
        return s[:n] == s[n+1:]

max_pal = -1
start = 999
for i in range(start,99,-1):
    for j in range(start,99,-1):
        if is_palindrom(i*j):
            if i*j>max_pal:
                max_pal = i*j
            break
print(max_pal)
