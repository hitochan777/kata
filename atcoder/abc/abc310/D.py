from collections import defaultdict

def sorted_k_partitions(seq, k):
    n = len(seq)
    groups = []  # a list of lists, currently empty
    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)
    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    result = sorted(result, key = lambda ps: (*map(len, ps), ps))
    return result 

N, T, M = (int(x) for x in input().split())  
ngs = defaultdict(set)
for _ in range(M):
  A, B = (int(x) for x in input().split())
  ngs[A].add(B)
  ngs[B].add(A)

ans = 0
for ps in sorted_k_partitions(range(1,N+1), T):
  # print(ps)
  ok = True
  for p in ps:
    n = len(p)
    if any(p[i] in ngs[p[j]] for i in range(n) for j in range(i+1,n)):
      ok = False
      break

  if ok:
    # print(ps)
    ans += 1

print(ans)
