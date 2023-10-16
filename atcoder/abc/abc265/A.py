X, Y, N = (int(x) for x in input().split())

three = min(X * 3, Y)

print((N // 3 * three) + (X * (N % 3)))