from collections import Counter
input() # ignore n
s = input()
n = Counter(s)["R"]
print(Counter(s[:n])["W"])
