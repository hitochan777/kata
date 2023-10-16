K, N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

B = [M * a // N for a in A]
diff = [(N * b - M * A[i], i) for i, b in enumerate(B)]
diff.sort()

R = M - sum(B)
for i in range(R):
  B[diff[i][1]] += 1

print(*B)
