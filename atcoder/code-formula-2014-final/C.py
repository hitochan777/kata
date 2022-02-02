import re
S = input()
names = set(re.findall(r"@\w+", S))
names = sorted(list(names))
for name in names:
  print(name[1:])