class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_N = len(nums)
        set_N = len(set(nums))
        if list_N == set_N:
            return False
        else:
            return True