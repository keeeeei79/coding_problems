# class Solution:
#     # brute force
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = -inf
#         for i in range(n):
#             cur_sum = 0
#             for j in range(i, n):
#                 cur_sum += nums[j]
#                 dp = max(dp, cur_sum)
#         return dp


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 4を加えた時に可能な配列の値は [-2, 1, -3], [1, -3], [-3]に4を足したもの
        # これは自分を含む配列で最大のもの
        # 最終的には4を加えた時に4を足した配列とそれまでの配列で大きい方を採用する
        ans = nums[0]
        max_include_me = [0] * n
        max_include_me[0] = nums[0]
        for i in range(1, n):
            max_include_me[i] = max(nums[i], nums[i] + max_include_me[i - 1])
            ans = max(ans, max_include_me[i])
        return ans
