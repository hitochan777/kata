N = int(input())
names = []
for _ in range(N):
  names.append(input().split(" "))

for i, (s, t) in enumerate(names):
  ok1 = all(s != names[j][0] and s != names[j][1] for j in range(N) if i != j)
  ok2 = all(t != names[j][0] and t != names[j][1] for j in range(N) if i != j)
  if not ok1 and not ok2:
    print("No")
    exit()

print("Yes")
    
