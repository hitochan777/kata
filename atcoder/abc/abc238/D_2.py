T = int(input())
for _ in range(T):
  a, s = (int(x) for x in input().split())
  if s-2*a < 0:
    print("No")
    continue

  if (s-2 * a) & a  == 0:
    print("Yes")
  else:
    print("No")