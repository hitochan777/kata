N = int(input())
X = list(int(x) for x in input().split())
X.sort()

print(sum(X[N:4*N])/(3*N))
