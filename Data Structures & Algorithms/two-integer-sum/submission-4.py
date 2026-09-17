class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myd = {}
        for idx,num in enumerate(nums):
            complement = target - num
            if complement not in myd:
                myd[num] = idx
                # print(num)
            else:
                # print('yes')
                return [myd[complement],idx]
        