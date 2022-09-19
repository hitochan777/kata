from textwrap import indent


A, B, C, D = 10, 10, 10, 10
cnt = 0
while cnt < 10:
  S = input()
  A = cnt+1
  cnt += 1
  start = S.find("#")
  if start < 0:
    continue

  C = start + 1
  end = S[start+1:].find(".")
  if end >= 0:
    D = end + start + 1
  
  break

while cnt < 10:
  S = input()
  if S.find("#") < 0:
    B = cnt
    break

  cnt += 1

print(A, B)
print(C, D)
