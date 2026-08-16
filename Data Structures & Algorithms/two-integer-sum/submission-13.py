class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for idx, n in enumerate(nums):
            if target - n in idx_map:
                return [idx_map[target-n], idx]
            idx_map[n] = idx

        
