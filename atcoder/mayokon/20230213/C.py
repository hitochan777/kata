from functools import lru_cache
N = int(input())
S = []
for _ in range(N):
    S.append(input())

S.reverse()

@lru_cache(maxsize=None)
def solve(n, t):
    if n == N:
        return 1

    ans = 0
    if t:
        if S[n] == "OR":
            ans += solve(n+1, True) * 2
            ans += solve(n+1, False)
        else:
            ans += solve(n+1, True)
    else:
        if S[n] == "OR":
            ans += solve(n+1, False)
        else:
            ans += solve(n+1, True)
            ans += solve(n+1, False) * 2

    return ans


print(solve(0, True))