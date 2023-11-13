from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(": ")", "{": "}", "[": "]"}
        stack = deque([])
        for c in list(s):
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0 or c != pair[stack.pop()]:
                    return False
        return len(stack) == 0
