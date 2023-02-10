from collections import Counter
S = input()
if len(S) == 1 or len(S) == 2:
    if int(S) % 8 == 0:
        print("Yes")
        exit()

if len(S) == 2:
    if int(S[::-1]) % 8 == 0:
        print("Yes")
        exit()

cnt = Counter(S)
for i in range(0, 1000, 8):
    cnt2 = Counter(str(i).zfill(3))
    if all(cnt[k] >= v for k, v in cnt2.items()):
        print("Yes")
        exit()

print("No")
