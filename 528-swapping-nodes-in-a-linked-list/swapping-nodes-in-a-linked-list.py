# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummNode = ListNode(-1)
        dummNode.next = head
        firstPointer = dummNode
        for i in range(k):
            firstPointer = firstPointer.next
        firstKth = firstPointer
        secondPointer = dummNode

        while(firstPointer):
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        
        temp = secondPointer.val
        secondPointer.val = firstKth.val
        firstKth.val = temp
        return dummNode.next   