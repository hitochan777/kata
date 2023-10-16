N = int(input())
A = list(int(x) for x in input().split())
A.sort()
B = list(int(x) for x in input().split())
ans = set() 

for a in A:
  x = a^B[0]
  C = list(map(lambda b: b^x, B))
  C.sort()
  if all(a == c for a, c in zip(A, C)):
    ans.add(x)

ans_li = list(ans)
ans_li.sort()
print(len(ans_li))
for val in ans_li:
  print(val)
