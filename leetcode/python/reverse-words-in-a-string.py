class Solution:
    def reverseWords(self, s: str) -> str:
        li = [item for item in s.strip().split(" ") if len(item) > 0]
        li.reverse()
        return " ".join(li)
