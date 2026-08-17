class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt_sort = sorted(cnt.keys(), key = lambda x:cnt[x],reverse=True )
        return cnt_sort[:k]