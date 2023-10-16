p, q = (x for x in input().split())

S = "ABCDEFG"
pos = [0, 3, 4, 8, 9, 14, 23]

a = S.find(p)
b = S.find(q)
print(abs(pos[a] - pos[b]))

