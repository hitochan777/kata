S = input()
N = len(S)
stack = []
for c in S:
  if len(stack) > 0 and stack[-1] != c:
    stack.pop()
    continue

  stack.append(c)

print(N - len(stack))