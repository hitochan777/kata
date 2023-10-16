from audioop import reverse


N, X, Y, Z = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())

passed = set()
for _, i in  sorted([(a, N-i) for i, a in enumerate(A)], reverse=True)[:X]:
  passed.add(N-i)

cnt = 0
for _, i in  sorted([(a, N-i) for i, a in enumerate(B)], reverse=True):
  if cnt < Y and N-i not in passed:
    passed.add(N-i)
    cnt += 1

cnt = 0
for _, i in  sorted([(a+b, N-i) for i, (a, b) in enumerate(zip(A, B))], reverse=True):
  if cnt < Z and N-i not in passed:
    passed.add(N-i)
    cnt += 1

for i in sorted(list(passed)):
  print(i+1)