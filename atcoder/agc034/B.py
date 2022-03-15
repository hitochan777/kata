import re
s = input()
ans = 0
s = s.replace("BC", "D")
matches = re.findall(r"[AD]+", s)
for match in matches:
  cnt = 0
  for c in match:
    if c == "A":
      cnt += 1
    else:
      ans += cnt
  
print(ans)