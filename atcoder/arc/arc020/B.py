n, c = (int(x) for x in input().split())
li = []
for _ in range(n):
  a = int(input())
  li.append(a)

min_cost = 10**18
for i in range(1, 11):
  for j in range(i+1, 11):
    t = [i, j]
    for offset in [0, 1]:
      cost = 0
      for k, a in enumerate(li):
        if a != t[(k+offset)%2]:
          cost += c

      min_cost = min(min_cost, cost)

print(min_cost)