class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myd = {}
        for i in range(len(nums)):
            # print(myd)
            # print(i)
            diff = target - nums[i]
            if diff in myd.keys():
                # print('yo')
                return [myd[diff],i]
            myd[nums[i]] = i
            

            
