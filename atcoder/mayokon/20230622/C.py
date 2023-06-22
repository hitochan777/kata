N, W = (int(x) for x in input().split())
li = [0] * (2*10**6)
for _ in range(N):
  S, T, P = (int(x) for x in input().split())
  li[S] += P
  li[T] -= P

for i in range(len(li)-1):
  li[i+1] += li[i]

for i in range(len(li)):
  if li[i] > W:
    print("No")
    exit()

print("Yes")