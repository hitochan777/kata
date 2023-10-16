from collections import defaultdict
def subString(s):
    cnt = defaultdict(int)
    cnt[0] = 1
    pre = 0
    count = 0
    for i in s:
        pre ^= (1 << (ord(i) - ord("0")))
        # print(bin(pre), cnt[pre])
        count += cnt[pre]
        cnt[pre] = cnt[pre] + 1

    return count
 
S = input()
print(subString(S))