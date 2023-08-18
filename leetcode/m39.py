class Solution:
    # 考え方としてはcandidatesから1つ要素を取り出してそれを必ず使うという条件で探索をする
    # 1つの要素を固定しての探索が終わったらその要素を除外するというのを繰り返す
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.dfs(candidates, target, [], output)
        return output

    def dfs(
        self,
        candidates: List[int],
        target: int,
        path: List[int],
        output: List[List[int]],
    ):
        # backtracking
        if target < 0:
            return
        if target == 0:
            output.append(path)
            return

        for i in range(len(candidates)):
            self.dfs(
                candidates[i:], target - candidates[i], path + [candidates[i]], output
            )
