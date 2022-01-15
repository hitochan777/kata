N = int(input())
H = list(int(x) for x in input().split())
p = 0

while p + 1 < N and H[p] < H[p+1]:
  p += 1

print(H[p])