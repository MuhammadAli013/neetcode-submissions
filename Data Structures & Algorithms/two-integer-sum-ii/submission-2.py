class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = first + 1
        for j in numbers[first:]:
            for i in numbers[second:]:
                second = first + 1
                if j == i:
                    continue
                # print(j,i)
                if j + i == target:
                    return [numbers.index(j)+1,numbers.index(i)+1]
            first += 1