class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        # nums = [2,20,4,10,3,4,5]
        nums = list(sorted(set(nums)))
        [n for n in nums if n-1 not in set(nums)]

        nums_seq_start = []
        idx_seq_start = []
        for idx in range(len(nums)):
            n = nums[idx]
            if n-1 not in set(nums):
                nums_seq_start.append(n)
                idx_seq_start.append(idx)


        print(nums)
        print('nums seq start',nums_seq_start)
        print('idx seq start',idx_seq_start)

        myd = {}
        for i in idx_seq_start:
            # just myd stuff
            n = nums[i]
            if not n in myd:
                myd[n] = []

            tmp_list = []
            tmp_list.append(n)
            for j in range(i+1,len(nums)):
                if nums[j-1] == nums[j]-1:
                    tmp_list.append(nums[j])
                else: break
            myd[n].append(tmp_list)
        # print(myd)
        myd_values_len = [len(myd[key][0]) for key in myd]
        print(myd)
        return max(myd_values_len)