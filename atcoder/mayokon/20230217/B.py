from collections import defaultdict
N = int(input())
d = defaultdict(int)
for _ in range(N):
    S = input()
    if S.startswith("!"):
        d[S[1:]] |= 2
    else:
        d[S] |= 1

for k, v in d.items():
    if v == 3:
        print(k)
        exit()

print("satisfiable")