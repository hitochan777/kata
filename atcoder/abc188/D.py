from collections import defaultdict

def solve():
    n, p = map(int, input().split())
    checkpoints = set()
    table = defaultdict(int) 
    cost = 0
    for _ in range(n):
        a, b, c = list((map(int, input().split())))
        table[a] += c
        table[b+1] -= c
        checkpoints.add(a)
        checkpoints.add(b+1)

    cps = sorted(list(checkpoints))
    for i in range(len(cps)-1):
        table[cps[i+1]] += table[cps[i]]

    for i in range(len(cps)-1):
        cost += min(p, table[cps[i]]) * (cps[i+1] - cps[i])

    return cost

print(solve())