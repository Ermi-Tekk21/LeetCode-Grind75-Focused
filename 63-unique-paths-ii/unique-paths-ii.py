class Solution:
    def uniquePathsWithObstacles(self, oG: List[List[int]]) -> int:
        m = len(oG)  # Number of rows
        n = len(oG[0])  # Number of columns

        # If the starting cell has an obstacle, return 0 (no possible path)
        if oG[0][0] == 1:
            return 0

        # Initialize the starting position as 2 instead of 1 (to handle integer division later)
        oG[0][0] = 2

        # Traverse the grid row-wise
        for i in range(m):
            for j in range(n):
                # Skip the first cell (already initialized) and obstacle cells (oG[i][j] & 1 checks if it is odd, i.e., an obstacle)
                if i == j == 0 or oG[i][j] & 1:
                    continue
                
                # Get the number of paths from the left and top cells
                left = 0 if (j < 1 or oG[i][j - 1] == 1) else oG[i][j - 1]
                top = 0 if (i < 1 or oG[i - 1][j] == 1) else oG[i - 1][j]

                # Store the total number of paths to reach this cell
                oG[i][j] = top + left

        # The answer is at the bottom-right cell, divide by 2 since we started with 2
        return oG[m - 1][n - 1] // 2