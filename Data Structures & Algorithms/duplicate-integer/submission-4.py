class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Solution with set length comparison
        #return len(set(nums)) != len(nums)

        #Solution with dictionary:
        numDict = {} #empty dictionary
        for i in range(len(nums)):
            numDict[nums[i]] = 1 + numDict.get(nums[i], 0)
            if numDict.get(nums[i], 0) > 1:
                return True
        return False
            
