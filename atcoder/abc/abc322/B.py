N, M = (int(x) for x in input().split())
S = input()
T = input()

val = 0
if T.endswith(S):
  val += 1

if T.startswith(S):
  val += 2

print(3-val)