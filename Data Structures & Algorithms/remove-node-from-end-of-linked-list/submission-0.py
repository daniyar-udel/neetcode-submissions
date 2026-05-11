# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        removeInd = len(nodes) - n
        if removeInd == 0:
            return head.next

        nodes[removeInd - 1].next = nodes[removeInd].next
        return head