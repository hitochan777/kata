from typing import Tuple

class Solution:
    def pad_right(self, a: str, b: str) -> Tuple[str, str]:
        max_len = max(len(a), len(b))
        return a.zfill(max_len), b.zfill(max_len)
        
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        
        a, b = self.pad_right(a, b)
        for i in range(len(b)-1, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            val, carry = s % 2, s // 2
            result = str(val) + result
            
        if carry == 1:
            result = "1" + result
            
        return result
