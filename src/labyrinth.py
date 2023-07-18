# Labyrinth cells constants
EMPTY = '.'
BLOCKED = '#'

# Rod orientation constants
HORIZONTAL = 0
VERTICAL = 1

class Labyrinth:

    '''
    Class the represents the labyrinth. It has information about the layout of the labyrinth and can check
    if the rod can do a certain movement.

    Parameters:
        labyrinth_map (List [List [str]]): A rectangular array that represents the layout of the labyrinth. 
                                           Cells marked with '.' are empty cells and those marked with '#' 
                                           are blocked.
    '''

    def __init__(self, labyrinth_map: list):
        self.labyrinth_map = labyrinth_map

    def can_the_rod_move_to_the_right(self, rod_state: dict):
        orientation = rod_state["rod_orientation"]
        x = rod_state["rod_center_position_x"] 
        y = rod_state["rod_center_position_y"]

        if orientation == HORIZONTAL:
            # Check if the rod is not touching the right wall of the labyrinth and
            # if the cell on the right of the rod is empty
            if x+2 < len(self.labyrinth_map[0]) and self.labyrinth_map[y][x+2] == EMPTY:
                return True
            else: 
                return False
            
        if orientation == VERTICAL:
            # Check if the rod is not touching the right wall of the labyrinth and
            # if the three cells on the right of the rod are all empty
            if x+1 < len(self.labyrinth_map[0]) and not any(BLOCKED in a[x+1] for a in self.labyrinth_map[y-1:y+2]):
                return True
            else: 
                return False
            
    def can_the_rod_move_to_the_left(self, rod_state: dict):
        orientation = rod_state["rod_orientation"]
        x = rod_state["rod_center_position_x"] 
        y = rod_state["rod_center_position_y"]

        if orientation == HORIZONTAL:
            # Check if the rod is not touching the left wall of the labyrinth and
            # if the cell on the left of the rod is empty
            if x-2 >= 0 and self.labyrinth_map[y][x-2] == EMPTY:
                return True
            else: 
                return False
            
        if orientation == VERTICAL:
            # Check if the rod is not touching the left wall of the labyrinth and
            # if the three cells on the left of the rod are all empty
            if x-1 >= 0 and not any(BLOCKED in a[x-1] for a in self.labyrinth_map[y-1:y+2]):
                return True
            else: 
                return False
            
    def can_the_rod_move_upwards(self, rod_state: dict):
        orientation = rod_state["rod_orientation"]
        x = rod_state["rod_center_position_x"] 
        y = rod_state["rod_center_position_y"]

        if orientation == HORIZONTAL:
            # Check if the rod is not touching the top wall of the labyrinth and
            # if the three cells above the rod are all empty
            if y-1 >= 0 and not any(BLOCKED in a[x-1:x+2] for a in self.labyrinth_map[y-1]):
                return True
            else: 
                return False
            
        if orientation == VERTICAL:
            # Check if the rod is not touching the top wall of the labyrinth and
            # if the cell above the rod is empty
            if y-2 >= 0 and self.labyrinth_map[y-2][x] == EMPTY:
                return True
            else: 
                return False
            
    def can_the_rod_move_downwards(self, rod_state: dict):
        orientation = rod_state["rod_orientation"]
        x = rod_state["rod_center_position_x"] 
        y = rod_state["rod_center_position_y"]

        if orientation == HORIZONTAL:
            # Check if the rod is not touching the bottom wall of the labyrinth and
            # if the three cells below the rod are all empty
            if y+1 < len(self.labyrinth_map) and not any(BLOCKED in a[x-1:x+2] for a in self.labyrinth_map[y+1]):
                return True
            else: 
                return False
            
        if orientation == VERTICAL:
            # Check if the rod is not touching the bottom wall of the labyrinth and
            # if the cell below the rod is empty
            if y+2 < len(self.labyrinth_map) and self.labyrinth_map[y+2][x] == EMPTY:
                return True
            else: 
                return False
            
    def can_the_rod_change_orientation(self, rod_state: dict):
        orientation = rod_state["rod_orientation"]
        x = rod_state["rod_center_position_x"] 
        y = rod_state["rod_center_position_y"]

        # Check if the rod is far away enough from the boundaries to rotate and 
        # if the cells in the 3x3 area surrounding it are all empty
        if (x+1 < len(self.labyrinth_map[0]) and x-1 >= 0 and 
                y+1 < len(self.labyrinth_map) and y-1 >= 0 and
                not any(BLOCKED in a[x-1:x+2] for a in self.labyrinth_map[y-1:y+2])):

            return True
        else:
            return False
