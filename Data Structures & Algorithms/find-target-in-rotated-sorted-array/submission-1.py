import bisect
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            m = (l +r) //2

            if nums[m] <= nums[-1]:
                r = m - 1
            else:
                l = m + 1

        return l
        
    def search(self, nums: List[int], target: int) -> int:
        m = self.findMin(nums)
        t1 = bisect.bisect_left(nums[:m], target)
        t2 = bisect.bisect_left(nums[m:], target)

        if t1 < m and nums[t1] == target:
            return t1

        if t2 < len(nums) - m and nums[m:][t2] == target:
            return t2+m
        
        return -1