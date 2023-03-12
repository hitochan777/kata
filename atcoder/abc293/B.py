N = int(input())
A = list(int(x)-1 for x in input().split())
called = set()
for i, a in enumerate(A):
  if i not in called:
    called.add(a)

ans = []
for i in range(N):
  if i not in called:
    ans.append(i+1)

print(len(ans))
print(*ans)
