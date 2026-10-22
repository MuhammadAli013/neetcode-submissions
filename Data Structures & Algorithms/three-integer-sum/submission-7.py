class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplet = []
        for i in range(0,len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            pairs = pair_sum_sorted_all(nums[i+1:],-1*nums[i])
            print(pairs)
            if len(pairs)>0:
                for pair in pairs:
                    triplet.append((nums[i],pair[0],pair[1]))
        return triplet
    
    
def pair_sum_sorted_all(p_nums,target):
    pairs = set()
    L = 0
    R = len(p_nums) - 1
    while L<R:
        summ = p_nums[L] + p_nums[R]
        if summ > target:
            R = R - 1
        elif summ < target:
            L = L + 1
        elif summ == target:
            pairs.add(tuple([p_nums[L],p_nums[R]]))
            L = L + 1
    return pairs
