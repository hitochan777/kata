M = int(input())
D = list(int(x) for x in input().split())
total = 0
target = (sum(D) + 1) // 2

for i, d in enumerate(D):
  if target <= total + d:
    print(i+1, target-total)
    exit()

  total += d