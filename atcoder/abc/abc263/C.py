N, M = (int(x) for x in input().split())

def enum(seq, start=1):
  if len(seq) == N:
    return [seq]

  seqs = []
  for i in range(start, M+1):
    seqs.extend(enum(seq + [i], i+1))

  return seqs

seqs = enum([])
seqs.sort()
for seq in seqs:
  print(*seq)
