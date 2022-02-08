s = input()

ans = 10**18
right = 10**18
for k in range(26):
  max_val = 0
  c = chr(ord("a") + k)
  for i in range(len(s)-1, -1, -1):
    if s[i] == c:
      right = i

    max_val = max(min(right - i, i), max_val)
  
  ans = min(max_val, ans) 

print(max_val)