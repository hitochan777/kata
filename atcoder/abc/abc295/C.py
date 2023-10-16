from collections import Counter
N = int(input())
cnt = Counter(int(x) for x in input().split())
ans = sum(v // 2 for v in cnt.values())
print(ans)


