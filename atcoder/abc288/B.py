N, K = (int(x) for x in input().split())
S = []
for _ in range(N):
    S.append(input())

for s in sorted(S[:K]):
    print(s)