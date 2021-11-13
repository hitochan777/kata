N, K = (int(x) for x in input().split())
cnt = [0] * (N + 2)
A = list(int(x) for x in input().split())
for a in A:
  cnt[1] += 1
  cnt[min(N, a)+1] += -1

total = 0
rem = 0
for i in range(1,N+2):
  cnt[i] += cnt[i-1]
  total += (cnt[i] + rem) // K
  if (cnt[i] + rem) // K > 0:
    rem = (cnt[i] + rem) % K

print(total)

