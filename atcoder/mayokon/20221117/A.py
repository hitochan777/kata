N = int(input())
P = list(int(x) for x in input().split())

ans = [0] * N
for i, p in enumerate(P):
  ans[i+1] = ans[p-1] + 1

print(ans[-1])
