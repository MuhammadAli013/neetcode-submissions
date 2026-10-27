class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set =  set(nums)
        answer = 0
        for n in nums_set:
            print(n)
            if n-1 not in nums_set:
                # print('yes')
                sq_len = 1
                # it's the starting
                while n+1 in nums_set:
                    # print('# yes')
                    sq_len = sq_len + 1
                    n=n+1
                answer = max(sq_len,answer)
        return answer