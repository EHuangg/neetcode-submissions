class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # save idx and val in stack
        # check if next value is non decreasing
        # if decrease: pop top items until stack is non decreasing again
        # calculate popped item area compare to max area
        # save the last popped item idx as starting idx for new item

        # if stack is non empty afterwards, calculate and compare remaining item areas

        stack = [] # non decreasing, [(idx, val)]
        max_area = 0

        for idx, val in enumerate(heights):
            if not stack or stack[-1][1] <= val:
                stack.append((idx, val))
            else:
                while stack and stack[-1][1] > val: # decreasing
                    area = stack[-1][1] * (idx - stack[-1][0]) # height * width
                    max_area = max(max_area, area)
                    starting_idx = stack.pop()[0]
                stack.append((starting_idx, val))
                
        
        for item in stack:
            area = item[1] * (len(heights) - item[0])
            max_area = max(max_area, area)

        return max_area

                
            