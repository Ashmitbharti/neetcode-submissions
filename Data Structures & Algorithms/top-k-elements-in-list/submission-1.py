class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for i in nums:
            c[i] = c.get(i,0) + 1
        s = sorted(c, key = c.get, reverse = True)

        return s[:k]
