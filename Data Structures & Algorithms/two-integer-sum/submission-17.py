class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myd = {}
        for i in range(len(nums)):
            x = nums[i]
            diff = target - x
            if diff in myd:
                return [myd[diff],i]
            myd[x] = i
            

            
