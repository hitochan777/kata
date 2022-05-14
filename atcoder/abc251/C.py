N = int(input())
subs = []
strs = set()
for i in range(N):
  S, T = input().split()
  T = int(T)
  if S not in strs:
    strs.add(S)
    subs.append((-T, i))

subs.sort()
print(subs[0][1] + 1)