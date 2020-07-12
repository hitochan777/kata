class Solution:
  def reverseBits(self, n: int) -> int:
    b = str(bin(n))[2:].rjust(32, '0')
    return int(b[::-1], 2)
                                
