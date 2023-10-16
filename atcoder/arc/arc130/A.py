N = int(input())
S = input()
 
prev = ""
total = 0
cnt = 0
for i in range(N):
  if prev != S[i]:
    total += cnt * (cnt-1) // 2
    cnt = 1
  else:
    cnt += 1
  
  prev = S[i]
 
total += cnt * (cnt-1)//2
print(total)