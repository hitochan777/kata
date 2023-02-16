S = input()
K = int(input())

nums = []
index = None
val = None
for i, c in enumerate(S, start=1):
  if c != "1":
    index = i
    val = c
    break

if index is None:
  print(S[0])
else:
  if K < index:
    print(1)
  else:
    print(val)


# 先頭が1以外のN→答えN
# 先頭が1→
# 1でないところが現れる最初の添字をiとする (1始まり)
# K < i -> 1
# K >= i → c