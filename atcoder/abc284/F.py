import math
class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

N = int(input())
T = input()
base = 26
mod = 2**60 - 1
rh = RollingHash(T, base, mod)
rh_rev = RollingHash(T[::-1], base, mod)

for i in range(N+1):
  h = (rh.get(0, i) * pow(base, N-i, mod) + rh.get(i+N, 2*N)) % mod
  rev_h = rh_rev.get(N-i, 2*N-i)
  if h == rev_h:
    print(T[:i] + T[i+N:], i)
    exit()

print(-1)