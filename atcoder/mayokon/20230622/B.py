O = list(input())
E = list(input())
if len(O) < len(E):
    O.append("")
elif len(E) < len(O):
    E.append("")

ans = ""
for o, e in zip(O, E):
    ans += o+e

print(ans)
