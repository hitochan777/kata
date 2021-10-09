N, P = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
print(sum(1 for a in A if a < P))