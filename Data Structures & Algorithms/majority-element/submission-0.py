class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
        
        for num in counter:
            if counter[num] >= len(nums) // 2:
                return num

        