S = input()
if S[0] == "1":
  print("No")
  exit()

m = {
  2: 2,
  3: 4,
  4: 1,
  5: 3,
  6: 5,
  7: 0,
  8: 2,
  9: 4,
  10: 6,
}

res = [False] * 7
for i in range(1,len(S)):
  res[m[i+1]] |= (S[i] == "1")

for i in range(7):
  if not res[i]:
    continue
  for j in range(i+2,7):
    if not res[j]:
      continue

    if all(not res[k] for k in range(i+1,j)):
      print("Yes")
      exit()

print("No")
