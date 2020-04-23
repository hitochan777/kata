class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m

        mb, nb = bin(m)[2:], bin(n)[2:]
        mb = mb.zfill(len(nb))
        m_0_index, n_0_index = mb.find("0"), nb.find("0")

        if n_0_index == -1:
            return 
        else:
            min(n_0_index, m_0_index)

        return n & m & (1 << (len(bin(n)[2:]) - 1))

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
