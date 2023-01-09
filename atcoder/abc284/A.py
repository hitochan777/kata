N = int(input())
S = []
for _ in range(N):
  S.append(input())

for s in S[::-1]:
  print(s)