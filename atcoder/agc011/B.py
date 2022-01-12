N = int(input())
A = list(int(x) for x in input().split())
A.sort()
acc = 0
cnt = 0
for i in range(N-1):
  if A[i+1] <= (acc + A[i]) * 2:
    cnt += 1
  else:
    cnt = 0
  
  acc += A[i]

print(cnt + 1)