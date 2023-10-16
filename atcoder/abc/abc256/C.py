h1, h2, h3, w1, w2, w3 = list(int(x) for x in input().split())

cnt = 0
for a11 in range(1,h1+1):
  for a12 in range(1, h1-a11+1):
    a13 = h1 - a11 - a12  
    if a13 <= 0:
      continue

    for a21 in range(1, h2+1):
      for a22 in range(1, h2-a21+1):
        a23 = h2 - a21 - a22
        if a23 <= 0:
          continue

        for a31 in range(1, h3+1):
          for a32 in range(1, h3-a31+1):
            a33 = h3 - a31 - a32
            if a33 <= 0:
              continue

            if w1 == a11 + a21 + a31 and w2 == a12 + a22 + a32 and w3 == a13 + a23 + a33:
              cnt += 1

print(cnt)