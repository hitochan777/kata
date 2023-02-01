N, X, M = (int(x) for x in input().split())
used = {X: 0}
f = [X]
idx = 1
repeat_from = None
while True:
  a = f[-1]
  b = (a**2) % M
  if b in used:
    # print(b, used[b])
    repeat_from = used[b]
    break
  
  used[b] = idx
  f.append(b)
  idx += 1

# print(f, repeat_from)

total = sum(f[:min(N, repeat_from)])
# print(total)
rem = N - min(N, repeat_from)
repeat_len = len(f) - repeat_from
# print(repeat_len)
total += (rem // repeat_len) * (sum(f[repeat_from:]))
total += sum(f[repeat_from:repeat_from+(rem%repeat_len)])

print(total)