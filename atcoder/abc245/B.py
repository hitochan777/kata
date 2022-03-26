N = int(input())
A = list(int(x) for x in input().split())
s = set(A)

n = 0
while n in s:
  n += 1

print(n)