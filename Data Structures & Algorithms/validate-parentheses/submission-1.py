class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in pairs:
                if not stk or stk[-1] != pairs[i]:
                    return False
                stk.pop()
            else:
                stk.append(i)
        return len(stk) == 0


