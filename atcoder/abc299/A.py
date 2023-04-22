N = int(input())
S = input()
isIn = False
for c in S:
    if c == "|":
      isIn = not isIn
    elif c == "*":
      if isIn:
         print("in")
         exit()

print("out")