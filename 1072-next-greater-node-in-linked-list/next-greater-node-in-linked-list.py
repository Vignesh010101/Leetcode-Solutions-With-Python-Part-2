# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        result  = {}

        temp = head
        i = 0

        while temp:
            result[i] = 0

            while stack and temp.val > stack[-1][1]:
                capture = stack.pop()
                result[capture[0]] = temp.val
            stack.append([i, temp.val])
            temp = temp.next
            i += 1

        return result.values()
        