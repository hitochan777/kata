N = int(input())
A = list(int(x) for x in input().split())

odds = [a for a in A if a % 2 == 1]
evens = [a for a in A if a % 2 == 0]

odds.sort()
evens.sort()
ans = -1
if len(odds) >= 2:
  ans = odds[-1] + odds[-2]

if len(evens) >= 2:
  ans = max(evens[-1] + evens[-2], ans)

print(ans)

