from rod import Rod

# Labyrinth cells constants
EMPTY = '.'
BLOCKED = '#'

class Labyrinth:

    '''
    Class the represents the labyrinth. It can check if the rod can do a certain movement and perform it.

    Parameters:
        
    '''

    def __init__(self, labyrinth_map):
        self.labyrinth_map = labyrinth_map
        #self.rod = Rod()
        self.rod = Rod(orientation=0, center_position_x=2, center_position_y=0)

    def can_the_rod_move_to_the_right(self):
        x = self.rod.center_position_x
        y = self.rod.center_position_y

        if self.rod.is_horizontal():
            if x+2 < len(self.labyrinth_map[0]) and self.labyrinth_map[y][x+2] == EMPTY:
                return True
            else: 
                return False
            
        if self.rod.is_vertical():
            if (x+1 < len(self.labyrinth_map[0]) and self.labyrinth_map[y][x+1] == EMPTY and 
                    self.labyrinth_map[y+1][x+1] == EMPTY and self.labyrinth_map[y-1][x+1] == EMPTY):
                return True
            else: 
                return False
            
    def can_the_rod_move_to_the_left(self):
        x = self.rod.center_position_x
        y = self.rod.center_position_y

        if self.rod.is_horizontal():
            if x-2 >= 0 and self.labyrinth_map[y][x-2] == EMPTY:
                return True
            else: 
                return False
            
        if self.rod.is_vertical():
            if (x-1 >= 0 and self.labyrinth_map[y][x-1] == EMPTY and 
                    self.labyrinth_map[y+1][x-1] == EMPTY and self.labyrinth_map[y-1][x-1] == EMPTY):
                return True
            else: 
                return False
            
    def can_the_rod_move_upwards(self):
        x = self.rod.center_position_x
        y = self.rod.center_position_y

        if self.rod.is_horizontal():
            if (y-1 >= 0 and self.labyrinth_map[y][x-] == EMPTY and 
                    self.labyrinth_map[y+1][x-1] == EMPTY and self.labyrinth_map[y-1][x-1] == EMPTY):
                return True
            else: 
                return False
            
        if self.rod.is_vertical():
            if y-2 >= 0 and self.labyrinth_map[y-2][x] == EMPTY:
                return True
            else: 
                return False

lab_map = ['#', '.', '.']
l = Labyrinth(lab_map)
print(l.can_the_rod_move_to_the_left())
l
