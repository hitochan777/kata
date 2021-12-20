K, T = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
print(max(2 * max(A) - 1 - K, 0))