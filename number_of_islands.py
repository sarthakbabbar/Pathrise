class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        self.grid = grid
        self.rows_len = len(grid)-1
        self.cols_len = len(grid[0])-1
        count = 0
        self.visitied = {}
        
        for row_index, row in enumerate(grid):
            for cell_index, cell in enumerate(row):
                if (row_index,cell_index) not in self.visitied:
                    if cell == "1":
                        count += 1
                        self.find_island(row_index,cell_index)
        return count            
    
    def find_island(self,row_index, cell_index):
        if row_index < 0 or row_index > self.rows_len:
            return True
        elif cell_index < 0 or cell_index > self.cols_len:
            return True
        elif (row_index,cell_index) in self.visitied:
            return True
        elif self.grid[row_index][cell_index] == "0":
            return True
        else:
            self.visitied[(row_index,cell_index)] = 1
            self.find_island(row_index+1,cell_index)
            self.find_island(row_index-1,cell_index)
            self.find_island(row_index,cell_index+1)
            self.find_island(row_index,cell_index-1)
            
            return True
        
                    
        
