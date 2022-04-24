N = int(input())
A = list(int(x) for x in input().split())

if N % 2 == 1:
  print("Win")
  exit()

xor = 0
for a in A:
  xor ^= a

if any(xor == a for a in A):
  print("Win")
else:
  print("Lose")
  