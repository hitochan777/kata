from collections import deque

S = input()
Q = int(input())
queue = deque(S)
is_reversed = False
for _ in range(Q):
    query = input().split()
    if len(query) == 1:
        is_reversed = not is_reversed
    else:
        c = query[2]
        should_append = (query[1] != "1") != is_reversed
        if should_append:
            queue.append(c)
        else:
            queue.appendleft(c)

ans = "".join(queue)
if is_reversed:
    ans = ans[::-1]

print(ans)