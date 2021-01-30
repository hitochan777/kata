A, B, C = list(map(int, input().split()))
if C == 0:
    A -= 1
else:
    B -= 1

print("Takahashi" if A >= B else "Aoki")