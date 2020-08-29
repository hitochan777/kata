class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            s2c = Counter(s2[i:i+len(s1)])
            if all(c in s2c and s2c[c] == freq for c, freq in s1c.items()):
                return True
            
        return False
