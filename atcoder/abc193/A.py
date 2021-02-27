# x = int(input())
A, B = (int(x) for x in input().split())
print((A - B) / A * 100)