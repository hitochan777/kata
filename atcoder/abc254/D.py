N = int(input())

ss = set()
i = 1
while i**2 <= N**2:
  ss.add(i**2)
  i += 1

print(len(ss))
# while i**2 <= N**2:
#   if i 