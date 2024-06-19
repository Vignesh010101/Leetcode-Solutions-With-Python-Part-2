class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        totalMin = mat[0][0]
        lenth = len(mat)

        for i in range(0, lenth):
            for j in range(0, lenth):
                if i > 0:
                    currentMin = mat[i - 1][j]
                    if j > 0:
                        currentMin = min(currentMin, mat[i - 1][j - 1])
                    if j < lenth - 1:
                        currentMin = min(currentMin, mat[i - 1][j + 1])
                    
                    mat[i][j] += currentMin;
                
                if i == lenth - 1:
                    if j == 0:
                        totalMin = mat[i][j]
                    else:
                        totalMin = min(totalMin, mat[i][j])
        
        return totalMin