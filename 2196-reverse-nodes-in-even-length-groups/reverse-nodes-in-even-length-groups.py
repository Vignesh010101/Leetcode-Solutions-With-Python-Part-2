# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getlen(self, head: Optional[ListNode]) -> int:
        itr = head
        c = 0
        while itr:
            c += 1
            itr = itr.next
        
        return c

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        last = None
        while curr:
            n = curr.next
            if n is None:
                last = curr
            curr.next = prev
            prev = curr
            curr = n
        head = prev
        itr = head
        while itr.next:
            itr = itr.next
        return [head, itr]

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        itr = head
        last = head
        length = self.getlen(head)
        while itr and length-count >= 0:
            if count % 2 == 0:
                first=itr
                last.next = None
                temp = 1
                while temp < count:
                    temp += 1
                    itr = itr.next
                else:
                    nxt = itr.next
                    itr.next = None
                    m, n = self.reverse(first)
                    last.next = m
                    n.next = nxt
                    last = n
                    itr = nxt
                length -= count
                count += 1
            else:
                if count == 1:
                    itr = itr.next
                    length -= count
                    count += 1
                else:
                    temp = 1
                    while temp <= count:
                        if temp == count-1:
                            last = itr.next
                        itr = itr.next
                        temp += 1
                    length -= count
                    count += 1
        
        if itr is not None:
            if length % 2 == 0:
                m, n = self.reverse(itr)
                last.next = m
                n.next = None
    
        return head