N = int(input())
li = []
for _ in range(N):
  A = int(input())
  li.append(A)

li.sort()

total = 0
if N % 2 == 0:
  i = 0
  for _ in range((N - 2) // 2):
    total += -2 * li[i]
    i += 1

  total += -li[i]
  i += 1
  total += li[i]
  i += 1
  for _ in range((N-2)//2):
    total += 2 * li[i]
    i += 1

else:
  total1 = 0
  i = 0
  for _ in range((N-2)//2+1):
    total1 += -2 * li[i]
    i += 1

  total1 += li[i]
  i += 1
  total1 += li[i]
  i += 1
  for _ in range((N-2)//2):
    total1 += 2 * li[i]
    i += 1

  total2 = 0
  i = 0
  for _ in range((N-2)//2):
    total2 += -2 * li[i]
    i += 1

  total2 -= li[i]
  i += 1
  total2 -= li[i]
  i += 1
  for _ in range((N-2)//2+1):
    total2 += 2 * li[i]
    i += 1 

  total = max(total1, total2)

print(total)



