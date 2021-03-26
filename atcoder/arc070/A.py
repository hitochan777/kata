X = int(input())

for i in range(1, 44722):
    if i * (i+1) // 2 >= X:
        print(i)
        break