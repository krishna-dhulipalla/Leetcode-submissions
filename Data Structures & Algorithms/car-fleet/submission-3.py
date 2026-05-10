class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]

        carfleet = len(position)
        prevtime = -1
        for p,s in sorted(pair)[::-1]:
            time = (target-p) / s
            if prevtime >= time:
                carfleet -= 1
            else:
                prevtime = time
            
        return carfleet