class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = max(heights)
        n = len(heights)

        leftMin = [n] * n
        stack = [] #idx
        rightMin = [-1] * n

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                leftMin[idx] = i

            if stack:
                rightMin[i] = stack[-1]

            stack.append(i)

        # print(leftMin)
        # print(rightMin)

        for i in range(n):
            maxArea = max(maxArea, heights[i] * (leftMin[i] - rightMin[i]-1))
        
        return maxArea