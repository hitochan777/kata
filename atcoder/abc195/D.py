N, M, Q = list(int(x) for x in input().split())
items = []
for _ in range(N):
    W, V = list(int(x) for x in input().split())
    items.append((V, W))

items.sort(reverse=True)

Xs = list(int(x) for x in input().split())

for _ in range(Q):
    L, R = list(int(x) for x in input().split())
    L -= 1
    R -= 1
    boxes = Xs[:L] + Xs[R+1:]
    boxes.sort()
    value = 0
    for item in items:
        for i, size in enumerate(boxes):
            if item[1] <= size:
                value += item[0]
                del boxes[i]
                break
    
    print(value)
