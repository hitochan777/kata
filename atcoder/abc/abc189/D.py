n = int(input())

cnt = 1
for i in range(n):
    op = input()
    if op == "OR":
        cnt = cnt + 2**(i+1)

print(cnt)