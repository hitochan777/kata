N = int(input())
A = []
B = []
for i in range(N):
  a, b = (int(x) for x in input().split())
  A.append((a, i))
  B.append((b, i))

A.sort(reverse=True)
B.sort(reverse=True)
li = [A, B]
ps = [0, 0]
eaten = set()
totals = [0, 0]
for i in range(N):
  p = i % 2
  while li[p][ps[p]][1] in eaten:
    ps[p] += 1

  eaten.add(li[p][ps[p]][1])
  totals[p] += li[p][ps[p]][0]

print(totals[0] - totals[1])

    
