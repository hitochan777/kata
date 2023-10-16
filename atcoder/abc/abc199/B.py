N = int(input())
l = max(int(x) for x in input().split())
h = min(int(x) for x in input().split())

print(max(h - l + 1, 0))


