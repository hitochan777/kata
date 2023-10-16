from collections import defaultdict

N = int(input())
A = list(int(x) for x in input().split())
n = min(N, 8)

lists = defaultdict(list)

for i in range(1<<n):
  total = 0
  seq = []
  for j in range(n):
    if (i >> j) & 1 == 1:
      seq.append(j+1)
      total += A[j]
      total %= 200
       
  if len(lists[total]) > 0:
    print("Yes")
    print(len(lists[total][0]), *lists[total][0])
    print(len(seq), *seq)
    exit()
  elif len(seq) > 0:
    lists[total].append(seq)
    
print("No")
  
  
      