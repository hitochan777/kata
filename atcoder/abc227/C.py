# for N in range(1,100):
#   cnt = 0
#   for a in range(1,100):
#     for b in range(a,100):
#       for c in range(b,100):
#         if a * b * c <= N:
#           # print(a,b,c)
#           cnt += 1

#   print(cnt)
  

N = int(input())

A_max = 1
while A_max**3 <= N:
  A_max += 1

cnt = 0
for a in range(1, A_max+1):
  B_max = int((N // a) ** (1/2))
  for b in range(a, B_max+1):
     cnt += N // (a * b) - b + 1

print(cnt)