T = int(input())
for _ in range(T):
  N = int(input())
  A = list(int(x) for x in input().split())
  ans = sum(1 for a in A if a % 2 == 1)
  print(ans)

