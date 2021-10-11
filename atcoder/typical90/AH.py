from collections import defaultdict

from collections import defaultdict

N, K = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

cnt = defaultdict(int)
start = 0
max_len = 0
for i, a in enumerate(A):
    cnt[a] += 1
    while len(cnt) > K:
        cnt[A[start]] -= 1
        if cnt[A[start]] == 0:
            del cnt[A[start]]

        start += 1

    max_len = max(max_len, i - start + 1)

print(max_len)