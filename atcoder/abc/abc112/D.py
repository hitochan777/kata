N, M = (int(x) for x in input().split())

def devisors(n: int):
    d = 1
    while d**2 <= n:
        if n % d == 0:
            yield d
            if d != n // d:
                yield n // d

        d += 1

d = 1
maxd = 0
for d in devisors(M):
    if N * d <= M:
        maxd = max(d, maxd)

print(maxd)