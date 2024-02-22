class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            return target in matrix[0]
        else:
            if target>=matrix[len(matrix)//2][0]:
                return self.searchMatrix(matrix[len(matrix)//2:],target)
            else:
                return self.searchMatrix(matrix[:len(matrix)//2],target)
        