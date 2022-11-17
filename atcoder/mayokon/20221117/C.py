N = int(input())
S = input()
acc = {
  "R": [0],
  "G": [0],
  "B": [0],
}

for i, c in enumerate(S):
  acc["R"].append(acc["R"][-1] + (1 if c == "R" else 0))
  acc["G"].append(acc["G"][-1] + (1 if c == "G" else 0))
  acc["B"].append(acc["B"][-1] + (1 if c == "B" else 0))

acc["R"] = acc["R"][1:]
acc["G"] = acc["G"][1:]
acc["B"] = acc["B"][1:]

# print(acc)

s = set(["R", "G", "B"])
ans = 0
for i in range(N):
  for j in range(i+1, N):
    if S[i] == S[j]:
      continue

    t = s - set([S[i], S[j]])
    rem = t.pop()
    cnt = acc[rem][-1] - acc[rem][j]
    k = j + (j-i)
    if k < N and S[k] == rem:
      cnt -= 1

    ans += cnt

print(ans)