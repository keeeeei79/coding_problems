class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = list("1234567890")
        sign = 1
        i = 0
        n = len(s)
        # 最初の空白を削除
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0

        # 記号を処理
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # 数字を処理
        ans = 0
        while i < n and s[i] in numbers:
            ans = ans * 10 + int(s[i])
            i += 1

        return min(2**31 - 1, max(-(2**31), sign * ans))


s = Solution()
print(s.myAtoi("+-43"))
