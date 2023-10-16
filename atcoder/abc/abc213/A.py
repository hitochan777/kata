A, B = (int(x) for x in input().split())

for c in range(2**8):
  if A^c == B:
    print(c)
    break