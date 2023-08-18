from types import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(nums: List[int], idx: int, result: List[int]):
            if idx >= len(nums):
                output.append(result)
                return
            dfs(nums, idx + 1, result + [nums[idx]])
            dfs(nums, idx + 1, result)

        dfs(nums, 0, [])
        return output
