N = int(input())
A = list(int(x) for x in input().split() if int(x) % 2 == 0)
print(*A)