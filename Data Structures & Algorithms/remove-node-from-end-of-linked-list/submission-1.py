# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        lst = []
        curr = head

        while curr:
            lst.append(curr)
            curr = curr.next

        removeInd = len(lst) - n
        if removeInd == 0:
            return head.next
        
        lst[removeInd - 1].next = lst[removeInd].next
        
        return head