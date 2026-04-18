class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return []
        time = [0] * len(position)
        for i in range(len(position)):
            time[i] = (position[i], (target - position[i]) / speed[i])
        time.sort()

        fleets = [time.pop()[1]]
        while time:
            top = time.pop()[1]
            if top > fleets[-1]:
                fleets.append(top)
        
        return len(fleets)
