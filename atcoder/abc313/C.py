N = int(input())
A = list(int(x) for x in input().split())

total = sum(A)
r = total % N
A.sort()
B = [total // N] * N
for i in range(r):
  B[N-1-i] += 1

ans = sum(abs(a - b) for a, b in zip(A, B)) // 2
print(ans)