N, S, T = (int(x) for x in input().split())
W = int(input())
diffs = [0]
for _ in range(N-1):
  A = int(input())
  diffs.append(A)

cnt = 0
for diff in diffs:
  W += diff
  if S <= W <= T:
    cnt += 1

print(cnt)


