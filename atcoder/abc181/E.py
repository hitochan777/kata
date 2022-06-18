from bisect import bisect_left


N, M = (int(x) for x in input().split())
H = sorted(list(int(x) for x in input().split()))
W = list(int(x) for x in input().split())

diff = [[],[]]
acc = [[0], [0]]
for i in range(N>>1):
  acc[0].append(acc[0][-1] + H[2*i+1] - H[2*i])

for i in range(N>>1):
  diff[1].append(H[N-2*i-1] - H[N-(2*i+1)-1])

diff[1] = diff[1][::-1]
for val in diff[1]:
  acc[1].append(acc[1][-1] + val)

ans = 10**18
for w in W:
  idx = bisect_left(H, w)
  a = acc[0][idx//2]
  b = acc[1][-1] - acc[1][idx//2]
  c = abs(H[idx-(idx%2)] - w)
  # print(idx, a,b,c)
  ans = min(a+b+c, ans)

print(ans)
