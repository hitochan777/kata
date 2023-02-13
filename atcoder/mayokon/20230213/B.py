from functools import lru_cache
L = int(input())

@lru_cache(maxsize=None)
def solve(L, N):
    if L == 0:
        if N == 0:
            return 1
        else:
            return 0
    if N == 0:
      return 0
    
    ans = 0
    for i in range(1, L-N+2):
      ans += solve(L-i, N-1)

    return ans

print(solve(L, 12))
        