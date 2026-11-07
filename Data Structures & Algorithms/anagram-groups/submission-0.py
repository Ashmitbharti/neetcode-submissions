class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key not in c:
                c[key]=[]
            
            c[key].append(i)
        return list(c.values())