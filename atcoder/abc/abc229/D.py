S = input()
n = len(S)
K = int(input())
totals = [0]
for i in range(n):
  totals.append(totals[i] + (1 if S[i] == "." else 0))

max_val = 0
r = 0
for l in range(n):
  while r < n and totals[r+1] - totals[l] <= K:
    r += 1

  max_val = max(max_val, r - l)

print(max_val)
  

  
