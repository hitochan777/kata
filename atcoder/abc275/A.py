N = int(input())
H = list((int(x), i+1) for i, x in enumerate(input().split()))
H.sort()

print(H[-1][1])