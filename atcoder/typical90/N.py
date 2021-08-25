N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
A.sort()
B.sort()

print(sum(abs(a-b) for a, b in zip(A, B)))
