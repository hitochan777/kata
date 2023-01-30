N, K = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

ng, ok = 0, 10**9+1
while ok-ng > 2*(10**(-6)):
    m = (ok+ng) / 2
    k = sum(a//m for a in A)
    if k <= K:
        ok = m
    else:
        ng = m

ans = list(int(a//ok) for a in A)
print(*ans)
