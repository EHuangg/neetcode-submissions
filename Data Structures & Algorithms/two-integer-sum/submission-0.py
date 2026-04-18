class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output = []
                    output.append(min(i, j))
                    output.append(max(i, j))
                    print (output)
                    return output
        print("wtf")
