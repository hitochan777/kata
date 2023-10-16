s = input()
cnt = 0
for i, c in enumerate(s):
    if i % 2 == 0:
        if c.islower():
            cnt += 1
    else:
        if c.isupper():
            cnt += 1

if cnt == len(s):
    print("Yes")
else:
    print("No")