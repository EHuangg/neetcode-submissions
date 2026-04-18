class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in sum_dict:
                return [sum_dict[num], i]
            else:
                sum_dict[target - num] = i
        