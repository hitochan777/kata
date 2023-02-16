O = input()
E = input()

ans = ""
for i in range(len(O)):
  if i < len(E):
    ans += O[i] + E[i]
  else:
    ans += O[i]

print(ans)

