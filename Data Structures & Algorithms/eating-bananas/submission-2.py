class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        n = len(piles)

        while l <= r:
            m = (l+r)//2
            
            time = 0
            for i in range(n):
                time += math.ceil(piles[i] / m)
            
            if time <= h:
                r = m - 1
            else:
                l = m + 1

        return l
