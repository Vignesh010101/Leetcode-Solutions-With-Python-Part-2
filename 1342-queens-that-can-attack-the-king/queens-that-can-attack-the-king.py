class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [['' for i in range(8)] for j in range(8)]
        ans = []
        
        # marking queens position on board
        for queen in queens:
            board[queen[0]][queen[1]] = 'Q'
            
        # marking kings position on board
        board[king[0]][king[1]] = 'K'
        
        for queen in queens:
            # function to check if a queen can target to king on board or not
            if self.canTarget(queen,king,board):
                ans.append(queen)
        return ans
    
    
    
    def canTarget(self,queen,king,board):
        q_x,q_y = queen[0],queen[1]
        
        # right side
        for i in range(q_y+1,8):
            if board[q_x][i] == 'K':
                return True
            elif board[q_x][i] == 'Q':
                break
                
        # left side
        for i in range(q_y-1,-1,-1):
            if board[q_x][i] == 'K':
                return True
            elif board[q_x][i] == 'Q':
                break
                
        # lower side
        for i in range(q_x+1,8):
            if board[i][q_y] == 'K':
                return True
            elif board[i][q_y] == 'Q':
                break
                
        # upper side
        for i in range(q_x-1,-1,-1):
            if board[i][q_y] == 'K':
                return True
            elif board[i][q_y] == 'Q':
                break
                
        # right down diagonal
        i,j = q_x+1,q_y+1
        while i<8 and j<8:
            if board[i][j] == 'K':
                return True
            elif board[i][j] == 'Q':
                break
            i += 1
            j += 1
            
        # left down diagonal
        i,j = q_x+1,q_y-1
        while i<8 and j>=0:
            if board[i][j] == 'K':
                return True
            elif board[i][j] == 'Q':
                break
            i += 1
            j -= 1
            
        # right up diagonal
        i,j = q_x-1,q_y+1
        while i>=0 and j<8:
            if board[i][j] == 'K':
                return True
            elif board[i][j] == 'Q':
                break
            i -= 1
            j += 1
            
        # left up diagonal
        i,j = q_x-1,q_y-1
        while i>=0 and j>=0:
            if board[i][j] == 'K':
                return True
            elif board[i][j] == 'Q':
                break
            i -= 1
            j -= 1
            
        # otherwise
        return False