class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_water = 0
        while L<R:
            water_amount = measure_water(L,R,heights)
            max_water = max(water_amount,max_water)
            left_height = heights[L]
            right_height = heights[R]

            if left_height < right_height:
                L = L + 1
            elif left_height > right_height:
                R = R - 1
            elif left_height == right_height:
                L = L + 1
                R = R - 1
        return max_water
    
def measure_water(L,R,heights):
    max_height = min(heights[L],heights[R])
    return (R-L)*max_height