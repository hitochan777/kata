class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for _ in range(k):
            i = 0
            while i < len(num) - 1 and int(num[i]) <= int(num[i+1]):
                i += 1

            num = num[:i] + num[i+1:]
        
        if len(num) == 0:
            return "0"
        return str(int(num))


if __name__ == "__main__":
    solver = Solution()
    assert solver.removeKdigits("1432219", 3) == "1219"
