N = int(input())
S = input()
stack = []
for c in S:
  stack.append(c)
  while len(stack) > 0 and stack[-1] == "x":
    if len(stack) >= 3 and "".join(stack[len(stack)-3:]) == "fox":
      stack.pop()
      stack.pop()
      stack.pop()
    else:
      break

print(len(stack))