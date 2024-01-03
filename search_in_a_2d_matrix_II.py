class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0])-1

        while r >= 0 and c >=0  and r < len(matrix) and c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r +=1 
        return False