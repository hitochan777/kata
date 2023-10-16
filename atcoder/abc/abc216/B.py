N = int(input())
s = set()
for _ in range(N):
  name = input()
  s.add(name)

if len(s) == N:
  print("No")
else:
  print("Yes")