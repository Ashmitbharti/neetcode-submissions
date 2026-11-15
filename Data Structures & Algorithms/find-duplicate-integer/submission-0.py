class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lookup = set()
        for i in nums:
            if i in lookup:
                return i
            else:
                lookup.add(i)
        return None