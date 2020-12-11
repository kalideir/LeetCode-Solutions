# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        carry = 0
        current = dummy_head
        p, q = l1, l2
        while(p or q):
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            last_digit = sum % 10
            newNode = ListNode(val=last_digit)
            current.next = newNode
            current = current.next
            if (p): p = p.next
            if (q): q = q.next
        if (carry > 0):
            current.next = ListNode(carry);
        return dummy_head.next;
