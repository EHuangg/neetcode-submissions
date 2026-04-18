class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            flag = 0
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    flag = 1
                    break
            res.append(count * flag)
        return res
