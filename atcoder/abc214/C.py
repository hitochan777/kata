N = int(input())
S = list(int(x) for x in input().split())
T = list(int(x) for x in input().split())

for i in range(2*N):
  T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])

for val in T:
  print(val)