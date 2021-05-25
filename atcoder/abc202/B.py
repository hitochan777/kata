S = input()
S = S[::-1]
result = ""
for c in S:
    if c in ["0", "1", "8"]:
        result += c
    elif c == "6":
        result += "9"
    else:
        result += "6"

print(result)
