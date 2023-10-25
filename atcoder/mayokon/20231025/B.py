def is_ok(s: str):
  n = len(s)
  return n % 2 == 0 and s[:n//2] == s[n//2:]

S = input()
for n in range(2, len(S)-2+1, 2):
  if is_ok(S[:-n]):
    print(len(S)-n)
    exit()