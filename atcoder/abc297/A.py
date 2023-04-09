N, D = (int(x) for x in input().split())
T = list(int(x) for x in input().split())
for i in range(N-1):
  if abs(T[i] - T[i+1]) <= D:
    print(T[i+1])
    exit()

print(-1)