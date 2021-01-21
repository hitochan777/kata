from collections import Counter

n = int(input())
al = list(map(int, input().split()))
q = int(input())
cnt = Counter(al)
total = sum(al)

for _ in range(q):
    b, c = list(map(int, input().split()))
    total += (c - b) * cnt[b]
    cnt[c] += cnt[b]
    cnt[b] = 0
    print(total)