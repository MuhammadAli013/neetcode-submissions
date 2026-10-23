class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = len(nums) - 1
        while L<R:
            num = nums[L]
            if num != 0:
                L=L+1
                continue
            else:
                nums.pop(L)
                nums.append(0)
                R=R-1
        