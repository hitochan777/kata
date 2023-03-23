N, K = (int(x) for x in input().split())
acc = [0]
for _ in range(N):
  t = int(input())
  acc.append(acc[-1]+t)

for i in range(2, N):
  if acc[i+1] - acc[i-2] < K:
    print(i+1)
    exit()
  
print(-1)

