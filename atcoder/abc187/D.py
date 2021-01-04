from collections import defaultdict
from typing import List
import math

def read_int() -> List[int]:
    return list(map(int, input().split(" ")))

def solve() -> str:
    diffs = []
    diff = 0
    n = read_int()[0]
    for _ in range(n):
        a, b = read_int()
        diffs.append(2 * a + b)
        diff -= a

    diffs.sort(reverse=True)
    cnt = 0
    while diff <= 0:
        diff += diffs[cnt]
        cnt += 1

    return cnt

print(solve())