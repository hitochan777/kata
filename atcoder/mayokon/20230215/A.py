N = int(input())
A = list(int(x) for x in input().split())

if all(a % 2 != 0 or a % 3 == 0 or a % 5 == 0 for a in A):
    print("APPROVED")
else:
    print("DENIED")