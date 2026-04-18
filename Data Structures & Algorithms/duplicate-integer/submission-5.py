class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                return True
            else:
                nums_dict[i] = 0
        return False