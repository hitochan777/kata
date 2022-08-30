N = int(input())
i = 1
while True:
  if i * (i+1) // 2 >= N:
    print(i)
    exit()

  i += 1