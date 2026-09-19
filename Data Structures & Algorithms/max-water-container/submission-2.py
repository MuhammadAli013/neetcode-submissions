class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculate_water(id1,h1,id2,h2):
            h = min(h1,h2)
            w = abs(id2 - id1)
            return h*w
        # heights = [1,7,2,5,4,7,3,6]
        # max_water = 0
        # for j,h_static in enumerate(heights):
        #     # print(j,h_static)
        #     for i in range(0,len(heights)):
        #         if i == j: continue
        #         h_dynamic = heights[i]
        #         water = calculate_water(j,h_static,i,h_dynamic)
        #         max_water = max(water,max_water)
        # return max_water
        max_water = 0
        L = 0
        R = len(heights) - 1
        while L<R:
            h1  = heights[L]
            h2 = heights[R]
            water = calculate_water(L,h1,R,h2)
            max_water = max(max_water,water)
            if h1<=h2:
                L = L + 1
            else:
                R=R-1
        return max_water