N, K = (int(x) for x in input().split())
comb = 6 * K * N - 6 * K**2 - 3 * N + 6 * K  - 2
print(comb/(N**3))