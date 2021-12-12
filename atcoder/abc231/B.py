from collections import defaultdict
N = int(input())
cnt = defaultdict(int)
for _ in range(N):
  S = input()
  cnt[S]+=1

li = list((value, key) for key, value in cnt.items())
li.sort()
print(li[-1][1])

