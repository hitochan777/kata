from collections import deque
Q = int(input())
mod = 998244353
mods = [1]
for _ in range(Q):
    mods.append((mods[-1] * 10)%mod)

s = 1
l = 1
q = deque()
q.append(1)
for _ in range(Q):
    arr = list(int(x) for x in input().split())
    cmd = arr[0]
    if cmd == 1:
      s = (10 * s + arr[1]) % mod
      q.append(arr[1])
      l += 1
    elif cmd == 2:
      val = q.popleft()
      s = (s - val * mods[l-1] + val * mod) % mod
      l -= 1
    else:
      print(s)