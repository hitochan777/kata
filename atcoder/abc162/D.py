from collections import Counter

N = int(input())
S = input()
d = Counter(S)

combs = d["R"] * d["G"] * d["B"]
complement = sum(1 for i in range(N) for j in range(i+1, N) if 2 * j - i < N and len(set([S[i], S[j], S[2 * j - i]])) == 3)

print(combs - complement)

