N = int(input())
D = list(int(x) for x in input().split())

ans = 0
for i, d in enumerate(D, start=1):
  for v in range(1, d):
    if len(set(list(f"{i}{v}"))) == 1:
      ans += 1

print(ans)