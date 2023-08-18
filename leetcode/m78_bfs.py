from types import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        idx = 0
        while idx < len(nums):
            result = self.bfs(nums, idx, result)
            idx += 1
        return result

    def bfs(
        self, nums: List[int], idx: int, subsets: List[List[int]]
    ) -> List[List[int]]:
        added = []
        for s in subsets:
            added.append(s + [nums[idx]])
        return subsets + added
