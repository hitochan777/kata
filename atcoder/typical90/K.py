from typing import List, Tuple

def get_reward(works: List[Tuple[int, int, int]]) -> Tuple[int, bool]:
  cur_date = 0
  reward = 0
  for work in works:
    cur_date += work[1]
    if cur_date > work[0]:
      return 0, False

    reward += work[2]

  return reward, True


N = int(input())
data = []
for _ in range(N):
  D, C, S = (int(x) for x in input().split())
  data.append((D, C, S))

data.sort()
max_reward = 0
for i in range(1 << N):
  subdata = []
  for j in range(N):
    if (i >> j) & 1 == 1:
      subdata.append(data[j])

  reward, solvable = get_reward(subdata)
  if solvable:
    max_reward = max(max_reward, reward) 

print(max_reward)
