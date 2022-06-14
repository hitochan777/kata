N = int(input())
A = list(int(x) for x in input().split())
A.sort()
B = list(int(x) for x in input().split())
ans = []
for i in A:
  x = B[0]^i
  C = list(map(lambda b: b^x, B))
  C.sort()
  if all(a == c for a, c in zip(A, C)):
    ans.append(x)

print(len(ans))
for val in ans:
  print(val)
