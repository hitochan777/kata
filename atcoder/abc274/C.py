N = int(input())
A = list(int(x) for x in input().split())
hist = [0] * (2*N+2)

for i, a in enumerate(A, start=1):
  if 2*i <= 2*N+1:
    hist[2*i] = hist[a] + 1

  if 2 * i + 1 <= 2 * N+1:
    hist[2 * i + 1] = hist[a] + 1

for i in range(1,2*N+2):
  print(hist[i])