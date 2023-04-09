S = input()
bi = []
ri = []
ki = None
for i, c in enumerate(S):
    if c == "B":
        bi.append(i)
    elif c == "K":
        ki = i
    elif c == "R":
        ri.append(i)

if (bi[0] % 2 != bi[1] % 2) and ri[0] < ki < ri[1]:
    print("Yes")
else:
    print("No")

