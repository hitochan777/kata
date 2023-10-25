N, X, Y = (int(x) for x in input().split())

def red(level, num):
  if level == 1:
    return 0

  return num * (red(level-1, 1) + blue(level, X))

def blue(level, num):
  if level == 1:
    return num

  return num * (red(level-1, 1) + blue(level-1, Y))

print(red(N, 1))