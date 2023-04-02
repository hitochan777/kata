S = input()
T = input()
chrs = "atcoder"
for s, t in zip(S, T):
    if s == t:
        continue

    if s == "@":
        if t in  chrs:
            continue
        else:
            print("You will lose")
            exit()
    elif t == "@":
        if s in chrs:
            continue
        else:
            print("You will lose")
            exit()
    else:
            print("You will lose")
            exit()

print("You can win")