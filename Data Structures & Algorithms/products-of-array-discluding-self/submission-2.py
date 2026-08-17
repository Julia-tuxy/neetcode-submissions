class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        cur = 1
        for i in range(1,n):
            cur = cur * nums[i-1]
            prefix[i] = cur
            
        cur = 1
        for i in range(n-2,-1,-1):
            cur = cur * nums[i+1]
            suffix[i] = cur

        res = []
        for i in range(n):
            product = prefix[i] * suffix[i]
            res.append(product)
        
        return res