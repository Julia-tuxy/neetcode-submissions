class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        seen = set()
        res = 1
        
        for n in nums:
            if n - 1 not in s:
                cur = 1

                while n + 1 in s:                
                    n += 1
                    cur += 1
                    res = max(res, cur) 
        
        return res
