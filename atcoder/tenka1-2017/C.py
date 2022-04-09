N = int(input())

def solve(N: int):
  for n in range(1, 3501):
    for h in range(1, 3501):
      nom = N * h * n
      denom = 4 * h * n - N * n - N * h
      if denom == 0:
        continue

      if nom % denom == 0:
        if nom // denom <= 0:
          continue

        return (h, n, nom // denom)

h, n, w = solve(N) 
print(h, n, w)