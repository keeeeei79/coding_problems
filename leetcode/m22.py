class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.dfs("", n, 0, 0, output)
        return output

    def dfs(self, s: str, n: int, left: int, right: int, output: List[str]):
        if len(s) == n * 2:
            output.append(s)
            return

        # left < nならまだleftを追加できる
        if left < n:
            self.dfs(s + "(", n, left + 1, right, output)

        if left > right:
            self.dfs(s + ")", n, left, right + 1, output)
