from itertools import accumulate

N, M, K = (int(x) for x in input().split())
a_list = (int(x) for x in input().split())
b_list = (int(x) for x in input().split())

a_acc = [0] + list(accumulate(a_list))
b_acc = [0] + list(accumulate(b_list))

max_val = 0
bp = M
for i in range(N+1):
    res = K - a_acc[i]
    if res < 0:
        continue

    while b_acc[bp] > res:
        bp -= 1

    max_val = max(max_val, i + bp)

print(max_val)