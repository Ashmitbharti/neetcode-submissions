class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup=set()
        for i in nums:
            if i not in lookup:
                lookup.add(i)
            else:
                return True
        return False