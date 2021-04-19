N, A, B = (int(x) for x in input().split())
Xs = [int(x) for x in input().split()]

cost = 0
for i in range(1, N):
    diff = Xs[i] - Xs[i-1]
    cost += min(diff * A, B)

print(cost)