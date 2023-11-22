N, Q = (int(x) for x in input().split())
C = list(int(x)-1 for x in input().split())
sets = [set([c]) for c in C]
for _ in range(Q):
  a, b = (int(x)-1 for x in input().split())
  sa, sb = sets[a], sets[b]
  if len(sb) < len(sa):
    sa, sb = sb, sa

  for val in sa:
    sb.add(val)

  new_set = sets[b]
  sets[a] = set()
  sets[b] = sb
  print(len(sb))


  