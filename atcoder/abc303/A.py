N = int(input())
S =  input()
T =  input()
if all(s == t or ((s == "1" and t == "l") or (s=="l" and t=="1")) or ((s == "0" and t == "o") or (s=="o" and t=="0")) for s, t in zip(S, T)):
  print("Yes")
else:
  print("No")
