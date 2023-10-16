R, C = (int(x) for x in input().split())
R, C = R-1, C-1
A1 = list(int(x) for x in input().split())
A2 = list(int(x) for x in input().split())
li = [A1, A2]
print(li[R][C])