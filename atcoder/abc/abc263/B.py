N = int(input())
P = [0] + list(int(x)-1 for x in input().split())
p = N-1
cnt = 0
while p != 0:
  p = P[p]
  cnt += 1

print(cnt)
