class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
            
        n = len(heights)
        l = 0
        r = n-1
        max_area = 0

        while l <= r:
            h = min(heights[l], heights[r])
            area = (r - l) * h
            max_area = max(max_area, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area