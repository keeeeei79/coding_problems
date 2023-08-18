class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4] -> [1,2,4,3]
        # [1,3,5,4,2] -> [1,4,2,3,5]
        # [1,1,5,4,2] -> [1,2,1,4,5]
        # [1,2,3,3,1] -> [1,3,1,2,3]
        # 最大のpermutationの時、つまり1の位が1番小さい時は配列を逆順にする
        # 手順としては
        # 1. nums[i] < nums[i+1]になってる場所を見つける
        # 2. nums[i]に変わって入れる数字を見つける
        # 3. i+1以降はnums[i+1]>nums[i+2]...となってるので入れ替える
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i - 1
        while nums[k] >= nums[j]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
