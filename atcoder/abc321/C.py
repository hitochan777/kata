K = int(input())
cnt = 0
s = set()

def solve(vals):
  if len(vals) >= 2:
    s.add(int("".join(map(lambda x: str(x), vals[1:]))))

  if len(vals) == 11 or vals[-1] == 0:
    return

  for i in range(vals[-1]):
    a = vals[:]
    a.append(i)
    solve(a)

solve([10])

li = sorted(list(s))[1:]
print(li[K-1])