class Solution:
    def numIslands(self, grid):
        count = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        flags = [([0] * len(grid[0])) for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flag = False
                if flags[i][j] == 0:
                    flags[i][j] = 1
                    if grid[i][j] == '1':
                        flags[i][j] = -1
                if grid[i][j] == '1':
                    if i > 0:
                        if flags[i-1][j] == -1:
                            flag = True
                        elif grid[i-1][j] == '1':
                            flags[i-1][j] = -1
                    if i < len(grid) - 1:
                        if flags[i + 1][j] == -1:
                            flag = True
                        elif grid[i+1][j] == '1':
                            flags[i+1][j] = -1
                    if j > 0:
                        if flags[i][j-1] == -1:
                            flag = True
                        elif grid[i][j-1] == '1':
                            flags[i][j-1] = -1
                    if j < len(grid[0]) - 1:
                        if flags[i][j+1] == -1:
                            flag = True
                        elif grid[i][j+1] == '1':
                            flags[i][j+1] = -1
                    if not flag:
                        count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]
    ]
    print(s.numIslands(grid))