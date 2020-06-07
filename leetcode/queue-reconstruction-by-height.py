class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda p: (-p[0], p[1]))
        for person in people:
            ans.insert(person[1], person)
            
        return ans
