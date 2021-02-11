S = input()
Q = int(input())
for _ in range(Q):
    query = input().split()
    if len(query) == 1:
        S = S[::-1]
    else:
        c = query[2]
        if query[1] == "1":
            S = c + S
        else:
            S = S + c

print(S)
