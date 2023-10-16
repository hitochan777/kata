H, W = (int(x) for x in input().split())

ans = 10**18
def update_min(val):
  global ans
  # print(val)
  ans = min(val, ans)

if H // 3 > 0:
  li = [H // 3] * 3
  rem = H % 3
  for i in range(rem):
    li[i] += 1
    
  update_min((max(li) - min(li)) * W)

if W // 3 > 0:
  li = [W // 3] * 3
  rem = W % 3
  for i in range(rem):
    li[i] += 1
    
  update_min((max(li) - min(li)) * H)
  
for h in range(1, H):
  li = [h * W, (H-h)*(W//2), (H-h)*((W//2)+W%2)]
  update_min(max(li) - min(li))
  li = [(H-h) * W, h*(W//2), h*((W//2)+W%2)]
  update_min(max(li) - min(li))
  
for w in range(1, W):
  li = [w * H, (W-w)*(H//2), (W-w)*((H//2)+H%2)]
  update_min(max(li) - min(li))
  li = [(W-w) * H, w*(H//2), w*((H//2)+H%2)]
  update_min(max(li) - min(li))
  
print(ans)