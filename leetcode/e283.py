class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        top_idx = 0
        a = nums[0]
        for i in range(1, len(nums)):
            b = nums[i]
            if a != 0 and b == 0:
                top_idx = i
            if a == 0 and b != 0:
                # nums[top_idx]とbを入れ替えてtop_idxをxxに書き換える
                nums[top_idx], nums[i] = nums[i], nums[top_idx]
                top_idx += 1
            a = nums[i]
