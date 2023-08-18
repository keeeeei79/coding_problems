class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx = 0
        sign = 1
        output = [[] for _ in range(numRows)]
        for c in s:
            output[idx].append(c)
            idx += sign
            if idx == 0:
                sign = 1
            elif idx == numRows - 1:
                sign = -1
        return "".join(["".join(x) for x in output])


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
