from collections import defaultdict, Counter
N = int(input())
cnt = Counter(input())

def ok(val, cnt):
  used = defaultdict(int)
  for c in val:
    if used[c] >= cnt[c]:
      return False

    used[c] += 1

  for k, v in cnt.items():
    if k == "0":
      continue

    if v - used[k] > 0:
      return False
  
  return True

ans = 0
#TODO:上限チェック
MAX = 10**7
# print(ok(str(1), cnt))
for i in range(0, MAX+1):
  if ok(str(i**2), cnt):
    # print(i**2)
    ans += 1

print(ans)