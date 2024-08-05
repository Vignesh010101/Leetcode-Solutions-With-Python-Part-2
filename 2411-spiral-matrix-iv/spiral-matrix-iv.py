# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix=[[-1]*n for i in range(m)]
        ROWS=0
        ROWE=m
        COLS=0
        COLE=n
        while head:
            for i in range(COLS,COLE):
                if not head:
                    return matrix
                matrix[ROWS][i]=head.val
                head=head.next
            ROWS+=1
            for i in range(ROWS,ROWE):
                if not head:
                    return matrix
                matrix[i][COLE-1]=head.val
                head=head.next
            COLE-=1
            for i in range(COLE-1,COLS-1,-1):
                if not head:
                    return matrix
                matrix[ROWE-1][i]=head.val
                head=head.next
            ROWE-=1
            for i in range(ROWE-1,ROWS-1,-1):
                if not head:
                    return matrix
                matrix[i][COLS]=head.val
                head=head.next
            COLS+=1
        return matrix