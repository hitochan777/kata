from collections import Counter

S = input()
if S.upper() != S and S.lower() != S and len(Counter(S)) == len(S):
  print("Yes")
else:
  print("No")
