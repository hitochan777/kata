from typing import List
import math
from functools import reduce

def get_min_stamps(n: int, blue_indices: List[int]):
    if len(blue_indices) == 0:
        return 1

    blue_indices.sort()
    if blue_indices[0] != 1:
        blue_indices.insert(0, 0)

    if blue_indices[-1] != n:
        blue_indices.append(n + 1)
    
    diffs = []
    for i in range(len(blue_indices) - 1):
        diff = blue_indices[i + 1] - blue_indices[i] - 1
        if diff == 0:
            continue

        diffs.append(blue_indices[i + 1] - blue_indices[i] - 1)

    if len(diffs) == 0:
        return 0

    k = min(diffs) 

    return sum(map(lambda diff: math.ceil(diff / k), diffs))

n, m = list(map(int, input().split()))
indices = list(map(int, input().split()))
ans = get_min_stamps(n, indices)
print(ans)

    


