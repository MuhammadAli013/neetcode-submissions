class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for j in range(0,len(numbers)):
            for i in range(j+1,len(numbers)):
                if numbers[j] + numbers[i] == target:
                    return [j+1,i+1]