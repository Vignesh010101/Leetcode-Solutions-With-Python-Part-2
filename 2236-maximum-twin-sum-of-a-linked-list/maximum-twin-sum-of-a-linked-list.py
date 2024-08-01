# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Initialize slow and fast pointers to head
        slow = fast = head
        # Initialize prev to None
        prev = None
        # Find middle of linked list using fast and slow pointer approach
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            # Reverse first half of linked list while traversing it
            slow.next = prev
            prev = slow
            slow = temp
            
        res = 0
        # Compare values of first and second half of linked list to find maximum twin sum
        while slow and prev:
            res = max(slow.val + prev.val, res)
            slow = slow.next
            prev = prev.next
        return res