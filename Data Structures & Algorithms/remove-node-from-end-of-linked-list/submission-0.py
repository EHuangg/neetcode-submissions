# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        target = 0
        while end:
            end = end.next
            target += 1
        target -= n # remove this index

        # navigate to target index
        prev, curr = None, head
        for i in range(target):
            prev = curr
            curr = curr.next
        
        # remove target:
        if not prev: # target is first element
            temp = curr.next
            curr.next = None
            head = temp
        elif not curr.next: # target is last element
            prev.next = None
            curr = prev
        else: # target is middle element
            temp = curr.next 
            prev.next = temp
            curr.next = None
            curr = temp
        return head