class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for idx, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                i, prev_t = stack.pop()
                res[i] = idx - i
            stack.append([idx, t])
        
        return res