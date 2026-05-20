# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        m = 1
        while l1:
            num1 += l1.val * m

            m *= 10
            l1 = l1.next

        m = 1
        while l2:
            num2 += l2.val * m

            m *= 10
            l2 = l2.next
    
        res = num1 + num2
        print(num1, num2)
        res = str(res)
        res = res[::-1]

        nodes = []
        for i in res:
            nodes.append(ListNode(int(i)))
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        return nodes[0]

