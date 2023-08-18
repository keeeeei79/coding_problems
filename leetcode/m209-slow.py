from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = 1e6
        for l in range(len(nums)):
            for r in range(l, len(nums) + 1):
                total = sum(nums[l:r])
                if total >= target:
                    output = min(output, r - l)
                    break
        return 0 if output > len(nums) else output


s = Solution()
s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
