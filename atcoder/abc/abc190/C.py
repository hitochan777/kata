from collections import defaultdict

N, M = list(map(int, input().split()))

conditions = []
for _ in range(M):
    conditions.append(list(map(int, input().split())))

max_val = 0
K = int(input())
persons = []
for _ in range(K):
    persons.append(list(map(int, input().split())))

for i in range(1 << K):
    chosens = set()
    for j in range(K):
        chosens.add(persons[j][(i >> j) & 1])

    max_val = max(max_val, sum(1 for a, b in conditions if a in chosens and b in chosens))

print(max_val)