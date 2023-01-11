class Solution:
    def isValid(self, s: str) -> bool:
        opcl = dict(("()", "[]", "{}"))
        stack = []
        for x in list(s):
            if x in "({[":
                stack.append(x)
            else:
                if len(stack) == 0 or x != opcl[stack.pop()]:
                    return False
        return len(stack) == 0
