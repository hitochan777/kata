N, X, Y = (int(x) for x in input().split())

def calc_max(level, red, blue):
  if level == 1:
    return blue

  cnt = 0
  if red > 0:
    cnt += red * calc_max(level-1, 1, 0)
    cnt += red * calc_max(level, 0, X)

  if blue > 0:
    cnt += blue * calc_max(level-1, 1, 0)
    cnt += blue * calc_max(level-1, 0, Y)
  return cnt

print(calc_max(N, 1, 0))