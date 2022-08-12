N = int(input())
robots = []
for _ in range(N):
  X, L = (int(x) for x in input().split())
  robots.append((X+L, X-L))

robots.sort()
cnt = 0
prev = -10**18
for robot in robots:
  if robot[1] >= prev:
    cnt += 1
    prev = robot[0]

print(cnt)