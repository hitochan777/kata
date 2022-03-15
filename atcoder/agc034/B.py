import re
s = input()
ans = 0
s = s.replace("BC", "D")
s = s.replace("AD", "E")
m = re.findall(r"E+", s)
for e in m:
  n = len(e)
  ans += n * (n+1) // 2
  
print(ans)