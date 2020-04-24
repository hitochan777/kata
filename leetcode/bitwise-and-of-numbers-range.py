class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m

        mb, nb = bin(m)[2:], bin(n)[2:]
        mb = mb.zfill(len(nb))

        ptr = -1
        for i in range(len(mb)):
            if mb[i] != nb[i]:
                break

            ptr = i

        bit_seq = nb[:ptr+1] + "0" * (len(mb) - ptr - 1)
        return int(bit_seq, 2)

if __name__ == "__main__":
    solver = Solution()
    result = solver.rangeBitwiseAnd(5,7)
    assert result == 4, result
    result = solver.rangeBitwiseAnd(0,1)
    assert result == 0, result
    result = solver.rangeBitwiseAnd(1,3)
    assert result == 0, result
    result = solver.rangeBitwiseAnd(100,100)
    assert result == 100, result
    result = solver.rangeBitwiseAnd(6,7)
    assert result == 6, result
    result = solver.rangeBitwiseAnd(10,11)
    assert result == 10, result
