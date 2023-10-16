N = int(input())
used = set()

while True:
  for n in range(1, 2 * N + 2):
    if n not in used:
      print(n, flush=True)
      used.add(n)
      break

  n = int(input())
  if n == 0:
    break
  used.add(n)

