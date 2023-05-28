# https://blog.hamayanhamayan.com/entry/2018/02/04/213426 がしっくり来た
N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
magic = 0
needs = 0
for a, b in zip(A, B):
  if a < b:
    magic += (b - a) // 2
  else:
    needs += a - b


if magic >= needs:
  print("Yes")
else:
  print("No")