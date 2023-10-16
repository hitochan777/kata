S = input()
for i in range(len(S)-1, -1, -1):
  if S[i] == "a":
    print(i+1)
    exit()

print(-1)