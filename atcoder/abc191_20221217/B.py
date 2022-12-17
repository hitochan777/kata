N, X = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
print(*[a for a in A if a != X])
