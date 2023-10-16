s = list(input())
K = int(input())
i = 0
while K > 0 and i < len(s):
  diff = (26 - (ord(s[i]) - ord("a"))) % 26
  if diff <= K:
    K -= diff
    s[i] = "a"

  i += 1

if K > 0:
  s[-1] = chr((ord(s[-1]) - ord("a") + K) % 26 + ord("a"))

print("".join(s))
