from collections import Counter
N = int(input())
A = list(int(x) for x in input().split())
cnt = Counter(A).items()
for i in range(len(cnt)):
    k1, v1 = cnt[i]
    for j in range(i+1, len(cnt)):
      k2, v2 = cnt[j]
