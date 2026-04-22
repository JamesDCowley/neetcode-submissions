# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        node_to_remove = length - n
        i = 0
        prev = head
        curr = head.next
        if node_to_remove != 0:
            while i != node_to_remove - 1:
                i += 1
                curr = curr.next
                prev = prev.next
            prev.next = curr.next
        # remove first node
        else:
            if head.next:
                head = head.next
            else:
                return None
        return head

        
        
        
        
        
