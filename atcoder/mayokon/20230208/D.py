N = int(input())
mxz, mnz, mxw, mnw = -10**18, 10**18, -10**18, 10**18
for _ in range(N):
  x, y = (int(x) for x in input().split())
  z = x + y
  w = x - y
  mxz, mnz = max(mxz, z), min(mnz, z)
  mxw, mnw = max(mxw, w), min(mnw, w)

print(max(mxz-mnz, mxw-mnw))
