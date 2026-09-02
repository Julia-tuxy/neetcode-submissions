class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        if not position:
            return 0

        n = len(position)
        
        cars = sorted(zip(position, speed), reverse=True)
        res = []


        for i in range(n):
            time = (target - cars[i][0]) / cars[i][1]
            if not res:
                res.append(time)
            if res and time > res[-1]:
                res.append(time)

        return len(res)