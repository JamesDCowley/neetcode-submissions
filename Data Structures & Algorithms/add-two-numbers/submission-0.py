# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        res_head = ListNode()
        res = res_head
        n1 = 0
        n2 = 0
        carry = 0
        while cur1 or cur2 or carry != 0:
            if cur1:
                n1 = cur1.val
                cur1 = cur1.next
            else:
                n1 = 0
            if cur2:
                n2 = cur2.val
                cur2 = cur2.next
            else:
                n2 = 0
            res_amt = (n1 + n2 + carry) % 10
            next_carry = (n1 + n2 + carry) // 10
            if next_carry != 0 or res_amt != 0:
                res.val = res_amt
                if cur1 or cur2 or next_carry != 0:
                    res.next = ListNode()
                    res = res.next
            carry = next_carry
        return res_head
            


                
