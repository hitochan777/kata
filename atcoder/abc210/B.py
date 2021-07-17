N = int(input())
S = input()
for i, c in enumerate(S):
  if c == "1":
    if i % 2 == 0:
      print("Takahashi")
    else:
      print("Aoki")
    
    break

  