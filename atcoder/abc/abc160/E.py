X, Y, A, B, C = list(map(int, input().split()))
ps = sorted(map(int, input().split()), reverse=True)
qs = sorted(map(int, input().split()), reverse=True)
rs = list(map(int, input().split()))

total = sum(sorted(ps[:X] + qs[:Y] + rs, reverse=True)[:X+Y])
print(total)