from collections import defaultdict
N = int(input())
A = list(int(x) for x in input().split())

cnt = defaultdict(int)
cnt[-1] = 3
ans = 1
for a in A:
  ans *= cnt[a-1]
  ans %= 1000000007
  cnt[a-1] -= 1
  cnt[a] += 1

print(ans)

# 0 0 1 0 1 1
# 3 2 2 1 2 1
# 6 * 6

