from collections import Counter, defaultdict
H, W = (int(x) for x in input().split())
g = []
row_cnt = defaultdict(lambda: defaultdict(int))
col_cnt = defaultdict(lambda: defaultdict(int))
for i in range(H):
  row = input()
  row_cnt[i] = Counter(row)
  g.append(row)

for j in range(W):
  col_cnt[j] = Counter(g[i][j] for i in range(H))

alive_row = set(list(range(H)))
alive_col = set(list(range(W)))
while True:
  marked = False
  remove_targets = []
  # print(row_cnt)
  for i in alive_row:
    if len(row_cnt[i]) == 1 and len(alive_col) >= 2:
      marked = True
      remove_targets.append(i)
      c = list(row_cnt[i].keys())[0]
      for j in alive_col:
        col_cnt[j][c] -= 1
        if col_cnt[j][c] == 0:
          del col_cnt[j][c]

      del row_cnt[i]
 
  # print("row", remove_targets)
  for i in remove_targets:
    alive_row.remove(i) 

  remove_targets = []
  # print(col_cnt)
  for i in alive_col:
    if len(col_cnt[i]) == 1 and len(alive_row) >= 2:
      marked = True
      remove_targets.append(i)
      c = list(col_cnt[i].keys())[0]
      for j in alive_row:
        row_cnt[j][c] -= 1
        if row_cnt[j][c] == 0:
          del row_cnt[j][c]

      del col_cnt[i]

  for i in remove_targets:
    alive_col.remove(i)

  # print("col", remove_targets)

  if not marked:
    break


row_num = len(alive_row)
col_num = len(alive_col)
print(row_num * col_num)