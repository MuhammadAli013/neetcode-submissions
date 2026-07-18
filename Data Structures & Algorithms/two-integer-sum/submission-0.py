class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j,N_outside in enumerate(nums):
            for i,N_inside in enumerate(nums):
                if i!=j:
                    if N_inside + N_outside == target:
                        return [j,i]