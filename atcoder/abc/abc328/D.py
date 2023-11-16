S = list(input())

stack = []
for c in S:
  if c == "C" and len(stack) >= 2 and stack[-2] == "A" and stack[-1] == "B":
    stack.pop()
    stack.pop()
  else:
    stack.append(c)
  
print("".join(stack))