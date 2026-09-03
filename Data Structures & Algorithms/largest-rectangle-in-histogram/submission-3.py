class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = max(heights)
        n = len(heights)

        leftMin = [n] * n
        stack = [] #idx

        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                leftMin[idx] = i
            stack.append(i)
        
        rightMin = [-1] * n
        stack = [] #idx
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                rightMin[idx] = i
            stack.append(i)



        for i in range(n):
            maxArea = max(maxArea, heights[i] * (leftMin[i] - rightMin[i]-1))
        
        return maxArea