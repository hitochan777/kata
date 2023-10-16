H, W, A, B = (int(x) for x in input().split())

def dfs(i, used, a, b):
  if i == H * W:
    return 1

  if (used >> i) & 1:
    return dfs(i+1, used, a, b)
   
  ans = 0
  if a > 0:
    if i % W != W - 1 and not (used & (1 << (i+1))):
      ans += dfs(i+1, used | (1 << i) | (1 << (i+1)), a-1, b)

    if i + W < H * W:
      ans += dfs(i+1, used | (1 << i) | (1 << (i+W)), a-1, b)
  
  if b > 0:
    ans += dfs(i+1, used | (1 << i), a, b-1)

  return ans

ans = dfs(0, 0, A, B)
print(ans)