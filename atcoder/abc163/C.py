n = int(input())
al = map(int, input().split())

cnts = [0] * n

for a in al:
    cnts[a-1] += 1

for cnt in cnts:
    print(cnt)

