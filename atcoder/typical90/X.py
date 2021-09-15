N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())

total = sum(abs(a - b) for a, b in zip(A, B))
if total <= K and abs(total - K) % 2 == 0:
  print("Yes")
else:
  print("No")

