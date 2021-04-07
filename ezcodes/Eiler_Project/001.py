sum = 0
last = 1000
for i in range(1,last):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)
#  after we get the answer, you can notice the regularity for different "last" values
#  10-23,100-2318,1000 - 233168, 10000-23331668,100000 - 2333316668 and so on
