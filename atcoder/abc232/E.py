H, W, K = (int(x) for x in input().split())
x1, y1, x2, y2 = (int(x) for x in input().split())
MOD = 998244353 

state = [1, 0, 0, 0]
for _ in range(K):
  new_state = [0] * 4
  new_state[0] = ((W-1) * state[1] + (H-1) *state[2]) % MOD
  new_state[1] = (state[0] + (W - 2) * state[1] + (H-1) * state[3]) % MOD
  new_state[2] = (state[0] + (H - 2) * state[2] + (W-1) * state[3]) % MOD
  new_state[3] = (state[1] + state[2] + (H-2+W-2) * state[3]) % MOD
  state = new_state

if (x1, y1) == (x2, y2):
  print(state[0])
elif x1 == x2:
  print(state[1])
elif y1 == y2:
  print(state[2])
else:
  print(state[3])