n, k = list(map(int, input().split()))
pl = list(map(int, input().split()))
pl.sort()
print(sum(pl[:k]))