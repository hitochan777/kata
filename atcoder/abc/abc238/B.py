N = int(input())
A = list(int(x) for x in input().split())
cur = 0
s = set()
s.add(0)
for a in A:
  cur += a
  cur %= 360
  s.add(cur)

li = sorted(list(s))
li.append(360)
print(max(li[i] - li[i-1] for i in range(1,len(li))))