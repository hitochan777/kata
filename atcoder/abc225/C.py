N, M = (int(x) for x in input().split())

def solve():
  prev_line = None
  for _ in range(N):
    line = list(int(x) for x in input().split())
    prev_val = None
    for val in line:
      if prev_val is not None:
        if val != prev_val + 1:
          return False

        if (val-1) // 7 != (prev_val-1) // 7:
          return False

      prev_val = val

    if prev_line is not None:
      ok = all(a == b + 7 for a, b in zip(line, prev_line))
      if not ok:
        return False
    
    prev_line = line

  return True

print("Yes" if solve() else "No")