N = int(input())
S = list(input().split())
for w in S:
    if w in ["and", "not", "that", "the", "you"]:
        print("Yes")
        exit()

print("No")