from collections import Counter
N = int(input())
lines = []
for _ in range(N):
  lines.append(input())

for i in range(N):
  for j in range(N-5):
    cnt = Counter(lines[i][j+k] for k in range(6))
    if cnt["."] <= 2:
      print("Yes")
      exit()

for i in range(N):
  for j in range(N-5):
    cnt = Counter(lines[j+k][i] for k in range(6))
    if cnt["."] <= 2:
      print("Yes")
      exit()

for i in range(N-5):
  for j in range(N-5):
    cnt = Counter(lines[i+k][j+k] for k in range(6))
    if cnt["."] <= 2:
      print("Yes")
      exit()

for i in range(N-5):
  for j in range(5, N):
    cnt = Counter(lines[i+k][j-k] for k in range(6))
    if cnt["."] <= 2:
      print("Yes")
      exit()

print("No")
