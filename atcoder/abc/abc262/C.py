N = int(input())
A = list(int(x) for x in input().split())
ans = 0
cnt = 0
s = set()
for i, a in enumerate(A, start=1):
  if i == a:
    cnt += 1
  elif A[a-1] == i:
    if (min(a, A[a-1]), max(a,A[a-1])) not in s:
      s.add((min(a, A[a-1]), max(a,A[a-1])))
      ans += 1

ans += cnt * (cnt-1) // 2
print(ans)
