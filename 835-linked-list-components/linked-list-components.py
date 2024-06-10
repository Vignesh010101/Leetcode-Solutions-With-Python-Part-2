# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        curr = head
        ans = 0
        if not curr:
            return ans
        while curr:    
            if curr.val in s and not (curr.next and curr.next.val in s):
                ans += 1
            curr = curr.next    
        return ans