class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums,target):
            'gives the two idxs for the target, the nums are sorted'
            left = 0
            right = len(nums) - 1
            solution = []
            while left < right:
                # print(left,right)
                if nums[left] + nums[right] == target:
                    # print('got it, the actual values are',left,right)
                    solution.append([nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                elif nums[left] + nums[right] < target:
                    left= left + 1
                elif nums[left] + nums[right] > target:
                    right = right - 1
            return solution
        nums = sorted(nums) # [-4, -1, -1, 0, 1, 2]
        # nums_copy = nums[:]
        All_solutions = []
        for i in range(len(nums)):
            n = nums[i]
            target_n = -1*n
            nums_copy = nums[i+1:]
            # print('dd')
            solution = two_sum(nums_copy,target_n)
            # print(solution)
            # nums_copy = nums[:]
            if len(solution) > 0:
                for sol in solution:
                    sol.extend([n])
                    sol = sorted(sol)
                    if sol not in All_solutions:
                        All_solutions.append(sol)
        return All_solutions