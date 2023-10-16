A, B, C, D, E, F = (int(x) for x in input().split())

max_val = 0
ans = None
for ca in range(0, 31):
  if 100*A*ca > F:
    break
  for cb in range(0, 16):
    if 100*A*ca + 100*B*cb > F:
      break

    for cc in range(0, 3001):
      if 100*A*ca + 100*B*cb +C*cc> F:
        break

      for cd in range(0, 1501):
        if 100*A*ca + 100*B*cb +C*cc + D*cd > F:
          break

        S = 100*A*ca + 100*B*cb + C*cc + D*cd
        if S == 0:
          continue

        if C*cc + D*cd > (A*ca + B*cb)*E:
          continue

        sugar = C*cc + D*cd
        max_val = max(max_val, 100 * sugar / S)
        if max_val == 100 * sugar / S:
          ans = (S, sugar)

print(*ans)

        