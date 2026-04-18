class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # with division:
        # find total product:
        zeros = 0
        total_prod = 1
        for i in nums:
            if i != 0:
                total_prod *= i
            else:
                zeros += 1
        
        prod_arr = []
        # disclude each item:
        for i in nums:
            if zeros == 0:
                prod_arr.append(int(total_prod/i))
            elif zeros == 1:
                if i == 0:
                    prod_arr.append(total_prod)
                else:
                    prod_arr.append(0)
            else:
                prod_arr.append(0)
        return prod_arr


