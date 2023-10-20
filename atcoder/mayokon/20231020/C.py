N, K = (int(x) for x in input().split())

def solve(score):
  if score >= K:
    return 1

  return solve(score*2)/2

prob = 0
for i in range(1, N+1):
  prob += 1/N * solve(i)

print(prob)

