from collections import Counter
N = int(input())
A = list(int(x) for x in input().split())
cnt = Counter(A)
print(len(cnt))
