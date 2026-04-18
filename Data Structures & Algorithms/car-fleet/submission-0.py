class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [3, 4.5, 10, 3]
        # [10, 4.5, 3, 3]
        # [0, 1, 4, 7]
        # combine lists, sort by position
        # calculate (target - position[i]) / speed
        # add to stack if time[i] <= time [i+1]
        # rerturn len(stack)

        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed = sorted(pos_speed, key = lambda x: x[0])
        times = []
        for i in range(len(pos_speed)):
            t = (target - pos_speed[i][0]) / pos_speed[i][1]
            times.append(t)
        
        stack = []
        for t in times:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return (len(stack))