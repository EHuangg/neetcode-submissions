class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (0, len(nums)):
            current = nums[i]
            #print (current)
            for j in range(i+1,len(nums)):
                temp = nums[j]
                print (temp)
                if current == temp:
                    return True
        return False