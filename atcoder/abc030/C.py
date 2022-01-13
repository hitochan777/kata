N, M = (int(x) for x in input().split())
X, Y = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
lists = [A, B]
c = [X, Y]
p = [0, 0]
s = 0
cnt = 0
t = lists[p[s]]

while p[s] < len(lists[s]):
  t = lists[s][p[s]] + c[s]
  s = (s+1) % 2
  if s == 0:
    cnt += 1

  while p[s] < len(lists[s]) and lists[s][p[s]] < t:
    p[s] += 1

print(cnt)


