S = input()
prev = 10
for c in S:
  if prev <= int(c):
    print("No")
    exit()

  prev = int(c)

print("Yes")