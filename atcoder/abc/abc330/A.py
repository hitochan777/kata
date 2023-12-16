N, L = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
ans = sum(1 for a in A if a >= L)
print(ans)