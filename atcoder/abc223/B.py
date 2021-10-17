S = input()
n = len(S)

min_str = S
max_str = S
for i in range(n):
  s = S[i:] + S[:i]
  min_str = min(min_str, s)
  max_str = max(max_str, s)

print(min_str)
print(max_str)