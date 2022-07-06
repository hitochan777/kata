N, M = (int(x) for x in input().split())

if M < 0 or M > N - 2:
  print(-1)
  exit()

for i in range(1,M+2):
  print(2*i, 2*i+1)

print(1, 2*(M+2))

base = 2*(M+2)
for i in range(N-(M+2)):
  print(2*i+1+base, 2*(i+1)+base)