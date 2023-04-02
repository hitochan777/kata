N = int(input())
H = list(int(x) for x in input().split())
prev = 0
for i in range(N):
  if prev < H[i]:
    H[i] -= 1

  if prev > H[i]:
    print("No")
    exit()

  prev = H[i]

print("Yes")