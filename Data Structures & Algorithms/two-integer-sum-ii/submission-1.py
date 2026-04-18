class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we can try 2 pointers, l = 0, r = len(numbers) - 1
        # if l + r < target: move min (l,r)
        #   - if min(l,r) = l: l += 1
        #   - else r -= 1
        # if l + r > target: move max (l,r)
        #   - if max(l,r) = l: l += 1
        #   - else r -= 1
        # if l + r == target: return [l + 1, r + 1]

        l, r = 0, len(numbers) - 1
        while l < r:
            left_num = numbers[l]
            right_num = numbers[r]
            print((left_num, right_num))
            if left_num + right_num < target:
                if min(left_num, right_num) == left_num:
                    l += 1
                else: 
                    r -= 1
            elif left_num + right_num > target:
                if max(left_num, right_num) == left_num:
                    l += 1
                else:
                    r -= 1
            else:
                return [l + 1, r + 1]

