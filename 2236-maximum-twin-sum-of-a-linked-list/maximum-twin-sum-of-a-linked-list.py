# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ls = []
        high=0
        while(head):
            ls.append(head.val)
            head=head.next
        l = len(ls)
        for i in range(int(l/2)):
                high = max(high,ls[i]+ls[l-1-i])
        return high
        