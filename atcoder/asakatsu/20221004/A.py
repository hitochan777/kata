S = input()
T = input()

print(sum(1 for a, b in zip(S, T) if a != b))