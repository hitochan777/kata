N, A, X, Y = list(int(x) for x in input().split())
print(min(A, N) * X + max(0, N - A) * Y)