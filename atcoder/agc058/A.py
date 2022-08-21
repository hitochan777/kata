N = int(input())
P = list(int(x) for x in input().split())

ans = []
for i in range(2*N-1):
  if i % 2 == 0:
    if P[i] > P[i+1]:
      if i == 2 * N - 2 or P[i] > P[i+2]:
        ans.append(i+1)
        P[i], P[i+1] = P[i+1], P[i]
      else:
        ans.append(i+2)
        P[i+1], P[i+2] = P[i+2], P[i+1]
  else:
    if P[i] < P[i+1]:
      if P[i] < P[i+2]:
        ans.append(i+1)
        P[i], P[i+1] = P[i+1], P[i]
      else:
        ans.append(i+2)
        P[i+1], P[i+2] = P[i+2], P[i+1]

print(len(ans))
print(*ans)