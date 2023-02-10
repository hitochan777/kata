from collections import Counter, defaultdict

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x)-1 for x in input().split()]

cc = Counter(C)
bc = defaultdict(int)
for i, b in enumerate(B):
    bc[b] += cc[i]

ans = 0
for i in range(N):
    ans += bc[A[i]]

print(ans)
