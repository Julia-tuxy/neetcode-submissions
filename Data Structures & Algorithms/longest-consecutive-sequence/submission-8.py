class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        seen = set()
        res = 1
        
        for n in nums:
            if n in seen:
                continue
            cur = 1
            seen.add(n)
            while n + 1 in s:                
                n += 1
                cur += 1
                res = max(res, cur) 
                seen.add(n)
        
        return res
