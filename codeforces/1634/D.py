import sys

def remove_impossible(target: list[int]) -> tuple[list[int], int]:
    pairs = []
    for i in range(4):
        query = ["?"]
        for j in range(4):
            if i == j:
                continue

            query.append(str(target[j]))

        print(" ".join(query))
        result = int(input())
        pairs.append((result, i))

    pairs.sort()
    removed = target[pairs[2][1]]
    target = [target[pairs[0][1]], target[pairs[1][1]]]
    return (target, removed)


def solve():
    n = int(input())
    target = [1, 2]
    removed = None
    for i in range(3, n + 1, 2):
        target.append(i)
        target.append(i + 1)
        target, removed = remove_impossible(target)

    if n % 2 == 1:
        target.append(n)
        target.append(removed)
        target, _ = remove_impossible(target)

    print("!", *target)
    sys.stdout.flush()


t = int(input())
for _ in range(t):
    solve()
