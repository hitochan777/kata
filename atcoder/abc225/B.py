from collections import defaultdict
cnt = defaultdict(int)
N = int(input())
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  cnt[A] += 1 
  cnt[B] += 1

ok = any(c == N-1 for _, c in cnt.items())
print("Yes" if ok else "No")