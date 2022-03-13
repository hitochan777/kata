N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())

print(sum(1 for a, b in zip(A, B) if a == b))
cnt = 0
for i in range(N):
  for j in range(N):
    if i == j:
      continue

    if A[i] == B[j]:
      cnt += 1

print(cnt)