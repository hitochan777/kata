from itertools import accumulate
from collections import Counter
from math import comb

input()
nums = [int(x) for x in input().split()]
cnts = Counter([0] + list(accumulate(nums)))
ans = sum(comb(cnt, 2) for _, cnt in cnts.items())
print(ans)
    
