N, X = (int(x) for x in input().split())
ans = 10**20
initial_total = 0
min_game_time = 10**20
for i in range(N):
  A, B = (int(x) for x in input().split())
  initial_total += A + B
  min_game_time = min(min_game_time, B)
  if X <= i + 1:
    ans = min(ans, initial_total)
    continue
  
  tmp = initial_total + (X - (i + 1)) * min_game_time
  ans = min(ans, tmp)

print(ans)
