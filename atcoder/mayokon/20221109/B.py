N = int(input())
H = list(int(x) for x in input().split())
level = 0
for i in range(1, N):
  if H[i-1] > H[i]:
    if H[i-1] - H[i] > 1 or level > 0:
      print("No")
      exit()

    level = 1
  elif H[i-1] < H[i]:
    level = 0

print("Yes")
