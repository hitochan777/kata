from math import floor
N = int(input())
 
def getSum(n):
    k =(n)**(.5)
    total = sum(floor(n / i) for i in range(1, floor(k) + 1))
    total *= 2
    total -= floor(k)**2
    return total


print(getSum(N))