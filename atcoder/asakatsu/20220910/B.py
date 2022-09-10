from math import gcd

W, H = (int(x) for x in input().split())
g = gcd(W, H)
W //= g
H //= g

print(f"{W}:{H}")