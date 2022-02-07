N = int(input())
for _ in range(N):
  n, k = (int(x) for x in input().split())
  even = n * k // 2
  odd = (n * k + 1) // 2
  if even % k != 0 or odd % k != 0:
    print("NO")
    continue
  
  print("YES")
  line = []
  for i in range(1, even+1):
    line.append(str(2 * i))
    if i % k == 0:
      print(" ".join(line))
      line = []

  line = []
  for i in range(1, odd+1):
    line.append(str((i-1) * 2 + 1))
    if i % k == 0:
      print(" ".join(line))
      line = []