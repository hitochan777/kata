N, P, Q = (int(x) for x in input().split())
A = min(list(int(x) for x in input().split()))
print(min(Q+A, P))