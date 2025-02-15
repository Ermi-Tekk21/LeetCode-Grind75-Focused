class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1  # Two-pointer approach
        max_area = 0
        
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            max_area = max(max_area, area)
            
            # Move the pointer with the smaller height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
