N = int(input())

ans = 0
for d in range(len(str(N))):
  a = (N // (10**d)) % 10
  for i in range(10):
    cnt = 0
    if i < a:
      cnt = (10**d)*(N//(10**(d+1))+1)
    elif i == a:
      cnt = (10**d)*(N//(10**(d+1))) + N % (10**d) + 1
    else:
      cnt = (10**d)*(N//(10**(d+1)))

    ans += cnt * i

print(ans)