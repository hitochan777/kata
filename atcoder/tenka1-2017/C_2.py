N = int(input())
# 4hnw = N(n*w + h*w + n*h) <= 4 * (3500**3)
# N <= 4*3500

for n in range(1, 3501):
  for h in range(1, 3501):
    w = int((4/N - 1/h - 1/n)**(-1))
    if 4*h*n*w == N*(n*w + h*w + n*h):
      print(h,n,w)
      exit()

