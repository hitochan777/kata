S = list(input())
T = list(input())
ok = False
for i in range(26):
  if all(chr(((ord(s) - ord("a")) + i) % 26 + ord("a")) == t for s, t in zip(S, T)):
    ok = True
    break

print("Yes" if ok else "No")
    
    