N = int(input())
min_val = 10 ** 10
for _ in range(N):
    A, P, X = (int(x) for x in input().split())
    if X - A <= 0:
        continue

    min_val = min(min_val, P)

print(min_val if min_val < 10 ** 10 else -1)
