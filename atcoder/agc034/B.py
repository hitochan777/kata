from urllib.request import AbstractBasicAuthHandler


s = input()
ans = 0
while s.count("ABC") > 0:
  c = s.count("ABC")
  ans += c
  s = s.replace("ABC", "BCA")

print(ans)