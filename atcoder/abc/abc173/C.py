h, w, k = map(int, input().split())
s = set()
for i in range(h):
    line = input()
    for j, c in enumerate(line):
        if c == "#":
            s.add((i, j))

def get_combs(li):
    if len(li) == 0:
        return [[]]

    combs = get_combs(li[:-1])
    return combs + [comb + [li[-1]]for comb in combs]

h_combs = get_combs(list(range(h)))
w_combs = get_combs(list(range(w)))
total = 0

for h_comb in h_combs:
    for w_comb in w_combs:
        cnt = sum(1 for i, j in s if i not in h_comb and j not in w_comb)
        if cnt == k:
            total += 1

print(total)