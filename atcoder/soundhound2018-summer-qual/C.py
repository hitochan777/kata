n, m, d = (int(x) for x in input().split())
tmp = 2*(n-d)/(n**2) if d != 0 else 1/n
ans = tmp * (m-1)
print(ans)
