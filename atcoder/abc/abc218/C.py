def rot90(S):
  return list(zip(*S[::-1]))

def find_left_top(S):
  for i, row in enumerate(S):
    for j, cell in enumerate(row):
      if cell == "#":
        # it is guaranteed that S contains at least one #
        return i, j

def is_same(S, T) -> bool:
  sti, stj = find_left_top(S)
  tti, ttj = find_left_top(T)
  offset_i, offset_j = tti - sti, ttj - stj
  for i, row in enumerate(S):
    for j, cell in enumerate(row):
      ii, jj = i + offset_i , j + offset_j
      if 0 <= ii < len(S) and 0 <= jj < len(row):
        if S[i][j] != T[ii][jj]:
          return False
      else:
        if S[i][j] == "#":
          return False

  return True

def solve():
  N = int(input())
  S = list()
  T = list()

  for _ in range(N):
    line = input()
    S.append(line)

  for _ in range(N):
    line = input()
    T.append(list(line))

  cnt_s = sum(1 for line in S for c in line if c == "#")
  cnt_t = sum(1 for line in T for c in line if c == "#")
  if cnt_s != cnt_t:
    print("No")
    return

  for _ in range(4):
    if is_same(S, T):
      print("Yes")
      return

    S = rot90(S)

  print("No")
  return

if __name__ == "__main__":
  solve()
