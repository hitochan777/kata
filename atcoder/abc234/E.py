X = int(input())

def gen():
  added = set()
  for f in range(1,10):
    for d in range(-9,9):
      s = ""
      c = f
      for _ in range(18):
        s += str(c)
        if int(s) not in added:
          yield int(s)
          added.add(int(s))

        c += d
        if c > 9 or c < 0:
          break

min_val = 10**18
for val in gen():
  if val >= X:
    min_val = min(min_val, val)

print(min_val)
