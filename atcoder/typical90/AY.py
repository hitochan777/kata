from collections import defaultdict
import bisect

N, K, P = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

fh = N >> 1
sh = N - fh

def get_info(n, offset):
  dic = defaultdict(list)
  for i in range(1 << n):
    cnt = 0
    total = 0
    for j in range(n):
      if (i >> j) & 1 == 1:
        cnt += 1
        total += A[j+offset]

    if cnt <= K:
      dic[cnt].append(total)

  for key in dic.keys():
    dic[key].sort()

  return dic

fd = get_info(fh, 0)
sd = get_info(sh, fh)

ans = 0
for i in range(K+1):
  for j in fd[i]:
    r = bisect.bisect_right(sd[K-i], P - j)
    ans += r

print(ans)