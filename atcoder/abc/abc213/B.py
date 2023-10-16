N = int(input())
A = (int(x) for x in input().split())
scores = sorted((a, i) for i, a in enumerate(A))
print(scores[-2][1] + 1)