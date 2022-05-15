N = int(input())

l, h = 0, N

print(0)
cur = input()
if cur == "Vacant":
  exit()

while True:
  m = (l + h) // 2
  if (l + m) % 2 == 0:
    target = cur
  else:
    target = "Female" if cur == "Male" else "Male"

  print(m)
  S = input()
  if S == "Vacant":
    exit()
  
  if S == target:
    l = m
    cur = S
  else:
    h = m