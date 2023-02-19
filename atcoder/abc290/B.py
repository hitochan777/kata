N, K = (int(x) for x in input().split())
S = input()

cnt = 0
ans = ""
for c in S:
    if c == "o" and cnt < K:
        ans += "o"
        cnt += 1
    else:
        ans += "x"

print(ans)