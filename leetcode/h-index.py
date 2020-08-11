class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for index in range(n,-1,-1):
            il = bisect_left(citations, index)
            ir = bisect_right(citations, index)
            if n - il >= index and n - ir <= index:
                return index
