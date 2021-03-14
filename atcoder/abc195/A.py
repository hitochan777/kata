# n = int(input())
M, H = list(int(x) for x in input().split())

if H % M == 0:
    print("Yes")
else:
    print("No")