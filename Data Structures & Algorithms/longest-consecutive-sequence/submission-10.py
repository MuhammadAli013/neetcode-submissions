class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        nums_set = set(nums)
        max_num = max(nums_set)
        print(nums_set)

        nums_seq_start = [n for n in nums_set if n-1 not in nums_set]
        print(nums_seq_start)

        myd = {}
        for n in nums_seq_start:
            if not n in myd:
                myd[n] = []
            tmp_list = []
            tmp_list.append(n)
            for n_next in range(n+1,max_num+1):
                if n_next in nums_set:
                    tmp_list.append(n_next)
                else: break
            # while n+len(tmp_list) in nums_set:
            #     tmp_list.append(n + len(tmp_list))
            myd[n].append(tmp_list)
        # print(myd)
        myd_values_len = [len(myd[key][0]) for key in myd]
        # print(myd)
        return max(myd_values_len)