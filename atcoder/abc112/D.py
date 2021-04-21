N, M = (int(x) for x in input().split())

d = 1
maxd = 0
while d**2 <= M:
    if M % d != 0:
        d += 1
        continue

    if N * d > M:
        break

    maxd = max(d, maxd)
    d += 1

print(maxd)