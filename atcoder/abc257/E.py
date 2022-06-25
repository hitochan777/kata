
N = int(input())
C = list(int(x) for x in input().split())
min_c = 10**18
min_i = 0
for i, c in enumerate(C, start=1):
  if min_c >= c:
    min_c = c
    min_i = i
    
ans = [str(min_i)] * (N // min_c)
rem = N % min_c
idx = 0
while rem > 0:
  for i in range(8, -1, -1):
    if min_i < i + 1 and 0 < C[i] - min_c <= rem:
      ans[idx] = str(i + 1)
      rem -= C[i] - min_c
      break
  else:
    break
  
  idx += 1

print("".join(ans))
   