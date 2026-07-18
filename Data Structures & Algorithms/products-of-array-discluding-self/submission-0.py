class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        for idx,i in enumerate(nums):
            multiply = 1
            nums_copy = nums.copy()
            nums_copy.pop(idx)
            for j in nums_copy:
                multiply = multiply * j
            lst.append(multiply)
        return lst