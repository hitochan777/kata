from collections import defaultdict

n = int(input())
al = list(map(int, input().split()))

cnt = defaultdict(int)
ok = defaultdict(lambda: True)
for a in al:
    cnt[a] += 1

for i in range(1, 10**6+1):
    if cnt[i] == 0:
        continue

    if cnt[i] > 1:
        ok[i] = False

    j = i * 2
    while j <= 10**6:
        ok[j] = False
        j += i

print(sum(1 for a in al if ok[a]))
