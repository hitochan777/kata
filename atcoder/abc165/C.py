N, M, Q = ( int(w) for w in  input().split() )

reqs = []
for _ in range(Q):
    reqs.append([int(w) for w in  input().split()])

def enum(lb, ub, n):
    if n == 1:
        return [[i] for i in range(lb, ub+1)]

    result = []
    for i in range(lb, ub + 1):
        subseqs = enum(i, ub, n - 1)
        result += [[i] + subseq for subseq in subseqs]

    return result

seqs = enum(1, M, N)
max_score = 0
for seq in seqs:
    score = sum(d for a, b, c, d in reqs if seq[b-1] - seq[a-1] == c)
    max_score = max(max_score, score)

print(max_score)