N = int(input())

if N == 0:
  print(0)
  exit()

ans = ""
while N != 0:
  if N % 2 != 0:
    N -= 1
    ans = "1" + ans
  else:
    ans = "0" + ans

  N /= -2

print(ans)