N = int(input())
l = len(str(N))

for i in range(1, 10 ** (l // 2) + 1):
    if int(str(i) * 2) > N:
        print(i - 1)
        break