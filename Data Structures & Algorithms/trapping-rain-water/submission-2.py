class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        
        cur = 0
        for i in range(1, n):
            cur = max(cur, height[i-1])
            prefix[i] = cur
        
        cur = 0
        for i in range(n-2,-1,-1):
            cur = max(cur, height[i+1])
            suffix[i] = cur
        
        total = 0
        for i in range(n):
            h = min(prefix[i],suffix[i])
            if h > height[i]:
                total += h - height[i]
        
        return total