# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        stack=[]
        maxi=0
        while(fast!=None and fast.next!=None):
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        while(len(stack)>0 and slow!=None):
            ele=stack.pop()
            if(ele+slow.val>maxi):
                maxi=ele+slow.val
            slow=slow.next
        return maxi