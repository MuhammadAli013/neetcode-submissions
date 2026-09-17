class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for j,N_outside in enumerate(nums):
        #     for i,N_inside in enumerate(nums):
        #         if i!=j:
        #             if N_inside + N_outside == target:
        #                 return [j,i]
        for j in range(len(nums)):
            for i in range(j+1,len(nums)):
                outnum = nums[j]
                innum = nums[i]
                if outnum + innum == target:
                    return [j,i]