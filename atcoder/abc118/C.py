from functools import reduce
import math
N = int(input())
A = list(int(x) for x in input().split())

print(reduce(lambda x,y: math.gcd(x,y), A, A[0]))