N = int(input())
V = list(int(x) for x in input().split())
C = list(int(x) for x in input().split())
ans = sum(max(v-c, 0) for v, c in zip(V,C))
print(ans)