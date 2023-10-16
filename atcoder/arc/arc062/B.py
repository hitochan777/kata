s = input()
r = 0
score = 0
for c in s:
  if c == "g":
    if r <= 0:
      r += 1
    else:
      r -= 1
      score += 1
  else:
    if r <= 0:
      r += 1
      score -= 1
    else:
      r -= 1

print(score)