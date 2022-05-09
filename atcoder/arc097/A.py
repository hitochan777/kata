s = input()
K = int(input())
substrs = set() 
for i in range(1,min(K, len(s))+1):
  for j in range(len(s)-i+1):
    substrs.add(s[j:j+i])

print(sorted(list(substrs))[K-1])