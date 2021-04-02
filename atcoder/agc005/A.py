X = input()

stack = []
for c in X:
    if c == "T" and len(stack) > 0 and stack[-1] == "S":
        stack.pop()
    else:
        stack.append(c)

print(len(stack))