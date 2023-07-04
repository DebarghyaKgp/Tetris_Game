import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_row=20
        self.num_col=10
        self.cell_size=30
        self.grid=[[0]*self.num_col for i in range(self.num_row)]
        self.colors=Colors.get_cell_colors()

    def print_grid(self):
        for row in self.grid:
            print(*row)

    def is_inside(self,row,column):
        if row>=0 and row<self.num_row and column>=0 and column<self.num_col:
            return True
        return False

    def is_empty(self,row,column):
        if self.grid[row][column]==0:
            return True
        return False

    def is_row_full(self,row):
        for i in self.grid[row]:
            if i==0:
                return False
        return True

    def clear_row(self,row):
        self.grid[row]=[0]*self.num_col

    def move_row_down(self,row,num_rows):
        for column in range(self.num_col):
            self.grid[row+num_rows][column]=self.grid[row][column]
            self.grid[row][column]=0

    def clear_full_rows(self):
        c=0
        for row in range(self.num_row-1,-1,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                c+=1
            elif c>0:
                self.move_row_down(row,c)
        return c

    def draw(self,screen):
        for row in range(self.num_row):
            for col in range(self.num_col):
                cell_value=self.grid[row][col]
                cell_rect=pygame.Rect(col*self.cell_size+11,row*self.cell_size+11,
                                      self.cell_size-1,self.cell_size-1 )
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect)

                
        
        

    
