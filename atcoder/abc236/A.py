S = input()
a, b = (int(x) for x in input().split())

print(S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:])