# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        p1_parent = None
        p1 = None
        p2_parent = None
        p2 = None
        counter = 1
        
        while curr:
            if counter == k:
                p1 = curr
            elif counter < k:
                p1_parent = curr
            
            if counter == 1:
                p2 = curr
            else:
                if counter >= k + 1:
                    if p2_parent:
                        p2_parent = p2_parent.next
                    else:
                        p2_parent = p2
                    p2 = p2.next
            
            curr = curr.next
            if curr:
                counter += 1

        if counter == 1:
            return head
        elif counter == 2:
            temp2 = head.next
            temp2.next = head
            head.next = None
            return temp2
        elif k == 1:
            p1_next = p1.next
            p2.next = p1_next
            p2_parent.next = p1
            p1.next = None
            return p2
        elif k == counter:
            p2_next = p2.next
            p1.next = p2_next
            p1_parent.next = p2
            p2.next = None
            return p1
        elif p1_parent is p2:
            p1_next = p1.next
            p2_parent.next = p1
            p1.next = p2
            p2.next = p1_next
            return head
        elif p2_parent is p1:
            p2_next = p2.next
            p1_parent.next = p2
            p2.next = p1
            p1.next = p2_next
            return head
        else:
            p1_next = p1.next
            p2_next = p2.next
            p1_parent.next = p2
            p2.next = p1_next
            p2_parent.next = p1
            p1.next = p2_next
            return head
   