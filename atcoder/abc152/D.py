from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
for i in range(1, n+1):
    num = str(i)
    cnt[(int(num[0]), int(num[-1]))] += 1

ans = sum(cnt[(i, j)] * cnt[(j, i)] for i in range(1, 10) for j in range(1, 10))
print(ans)