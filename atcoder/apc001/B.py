N = int(input())
As = list(int(x) for x in input().split())
Bs = list(int(x) for x in input().split())

cnt = 0
for a, b in zip(As, Bs):
    if a < b:
        cnt += (b - a) // 2
    else:
        cnt -= a - b

if cnt < 0:
    print("No")
else:
    print("Yes")