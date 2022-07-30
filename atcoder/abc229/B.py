A, B = (int(x) for x in input().split())
C = str(A + B)
A = str(A).zfill(len(C))
B = str(B).zfill(len(C))

for a, b, c in zip(A, B, C):
  if int(a) + int(b) < int(c):
    print("Hard")
    exit()

print("Easy")
