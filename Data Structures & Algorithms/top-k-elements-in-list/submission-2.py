class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            #print (count)
        
        #sorting
        arr = []
        for val, cou in count.items():
            arr.append([cou, val])
            #print (arr)
        arr = sorted(arr, reverse = True)
        
        res = []
        print (arr)
        for i in range(k):
            res.append(arr[i][1])
            print (res)
        return res