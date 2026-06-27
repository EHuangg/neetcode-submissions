class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colour_count = {0:0, 1:0, 2:0}
        for n in nums:
            colour_count[n] += 1

        i = 0
        for n in range(0,3):
            while colour_count[n] > 0:
                nums[i] = n
                colour_count[n] -= 1
                i += 1
