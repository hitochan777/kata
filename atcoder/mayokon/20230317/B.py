from collections import defaultdict
N = int(input())
A = list(int(x) for x in input().split())

steps = defaultdict(int)
for i, a in enumerate(A, start=1):
    steps[2*i] = steps[a] + 1
    steps[2*i+1] = steps[a] + 1

for i in range(1, 2*N+2):
    print(steps[i])