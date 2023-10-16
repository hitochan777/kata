T = int(input())
for _ in range(T):
  N = int(input())
  S = input()
  cnt =  S.count("1")
  if cnt % 2 == 1:
     print(-1)
  elif cnt == 2 and "11" in S:
    if len(S) <= 3:
      print(-1)
    elif S == "0110":
      print(3) 
    else:
      print(2)
  else:
      print(cnt//2)