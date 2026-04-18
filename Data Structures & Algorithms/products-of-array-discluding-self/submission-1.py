class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1]
        suffix = [1]
        for i in range (0, len(nums)-1):
            prefix.append(prefix[-1] * nums[i])
        
        for i in range (len(nums)-1,0,-1):
            suffix.append(suffix[-1] * nums[i])
        suffix = suffix[::-1]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res


