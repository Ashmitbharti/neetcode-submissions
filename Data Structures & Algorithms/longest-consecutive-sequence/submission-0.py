class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = set(nums)
        l = 0
        for i in c:
            if i-1 not in c:
                curr = i
                le=1
                while curr + 1 in c:
                    le += 1
                    curr += 1
                l = max(l,le)
        return l
      