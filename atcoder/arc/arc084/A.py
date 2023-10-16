from bisect import bisect_right


N = int(input())
A = sorted(list(int(x) for x in input().split()))
B = sorted(list(int(x) for x in input().split()))
C = sorted(list(int(x) for x in input().split()))
B2 = [0]

for b in B[::-1]:
  idx = bisect_right(C, b)
  B2.append(N - idx + B2[-1])

B2 = B2[::-1]
ans = 0
for a in A:
  idx = bisect_right(B, a)
  ans += B2[idx]

print(ans)

