n = input()
k = len(n)

min_val = k 
for i in range((1<<k)-1):
    s = []
    mask = i
    for j in range(k):
        if mask & 1 == 0:
            s.append(n[j])

        mask >>= 1

    if int("".join(s)) % 3 == 0:
        min_val = min(min_val, k - len(s))

if min_val == k:
    print(-1)
else:
    print(min_val)