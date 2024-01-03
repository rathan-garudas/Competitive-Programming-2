class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) 
        m = len(matrix[0])
        l, h = 0, n * m

        while l <= h and l >= 0 and l < n*m and h >= 0  and h <= n*m:
            mid = l + (h-l)//2
            r = mid // m
            c = mid % m

            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                h = mid - 1
            else:
                l = mid + 1
                
        
        return False