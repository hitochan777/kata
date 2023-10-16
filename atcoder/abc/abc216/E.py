from collections import Counter
N, K = (int(x) for x in input().split())
cnt = Counter(int(x) for x in input().split())
A = [(int(k), v) for k, v in cnt.items()]
A.sort(reverse=True)
A.append((0, 0))
cur = 0
ans = 0

def total(n):
  return n * (n+1) // 2

while K > 0 and cur < len(A) - 1:
  val, cnt = A[cur]
  # print(cur, N, A)
  nxt_val, nxt_cnt  = A[cur+1]
   
  if (val - nxt_val) * cnt <= K:
    ans += (total(val) - total(nxt_val)) * cnt
    K -= (val - nxt_val) * cnt
    A[cur+1] = (nxt_val, nxt_cnt+cnt)
  else:
    d, m = divmod(K, cnt)
    ans += (total(val) - total(val-d)) * cnt + (val-d) * m
    K = 0

  cur += 1

print(ans)