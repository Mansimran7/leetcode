class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if target < matrix [0][0]:
            return False
        elif target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False
        
        low_col = 0 
        high_col = len(matrix)-1

        row = len(matrix[0])-1

        while(low_col < high_col):
            mid_col = (low_col + high_col)//2
            print("col", matrix[mid_col][0], matrix[mid_col][row])
            print(mid_col, low_col, high_col)
            if matrix[mid_col][0] == target:
                return True
            
            elif matrix[mid_col][0] < target:
                if matrix[mid_col][row] >= target:
                    high_col = low_col = mid_col
                else:
                    low_col = mid_col + 1

            else:
                high_col = mid_col - 1
        
        col = high_col 
        print(col)
        low_row = 0 
        high_row = len(matrix[0])-1

        while (low_row <= high_row):
            mid_row = (low_row + high_row)//2

            if matrix[col][mid_row] == target:
                return True
            elif matrix[col][mid_row] < target:
                low_row = mid_row + 1
            else:
                high_row = mid_row - 1
        return False 
        
