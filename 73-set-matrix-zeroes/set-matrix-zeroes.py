class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def find1(mat):
            s = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j]==0:
                        s.append([i,j])
            return s
        def setting(mat,i,j):
            for z in range(len(mat[0])):
                mat[i][z] = 0
            for z in range(len(mat)):
                mat[z][j]=0
        vis = find1(matrix)
        for i,j in vis:
            setting(matrix,i,j)
            