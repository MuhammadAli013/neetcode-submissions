class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        if nums == [] : return 0
        # print(nums)
        myd = {}
        for i in range(len(nums)):
            n = nums[i]
            # just myd stuff
            if not n in myd:
                myd[n] = []

            tmp_list = []
            tmp_list.append(nums[i])
            for j in range(i+1,len(nums)):
                if nums[j]-1 in nums:
                    tmp_list.append(nums[j])
                else: break
            myd[n].append(tmp_list)
        # print(myd)
        myd_values_len = [len(myd[key][0]) for key in myd]
        return max(myd_values_len)