x, n = list(map(int, input().split()))
pl = set(map(int, input().split()))
min_val = 102
min_num = -1
for i in range(0, 102):
    if i not in pl:
        if min_val > abs(x - i):
            min_val = abs(x - i)
            min_num = i

print(min_num)
