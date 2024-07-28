class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        board = [['.']*10] + [                     
                 ['.']+row+['.'] for row in board]+ [ 
                 ['.']*10]

        other = 'B' if color == 'W' else 'W'

        dir = ((-1,-1), (-1,0), (-1, 1),            
               ( 0,-1),         ( 0, 1),
               ( 1,-1), ( 1,0), ( 1, 1))

        for dr, dc in dir:

            r, c = rMove + 1 + dr, cMove + 1 + dc   
            if board[r][c] != other: continue       

            while board[r][c] == other:             
                r+= dr                             
                c+= dc

            if board[r][c] == color: return True    
        return False