for i in range(8):
  S = input()
  j = S.find("*")
  if j < 0:
    continue

  print(chr(ord("a") + j) + str(8 - i))