
# Rod orientation constants
HORIZONTAL = 0
VERTICAL = 1

class rod:    

    def __init__(self, orientation=HORIZONTAL, center_position_x=1, center_position_y=0):
        if orientation == HORIZONTAL or orientation == VERTICAL:
            self.orientation = orientation
        else:
            self.orientation = HORIZONTAL

        self.center_position_x = center_position_x
        self.center_position_y = center_position_y

    def move_to_the_right(self):
        self.center_position_x += 1

    def move_to_the_left(self):
        self.center_position_x -= 1
    
    def move_upwards(self):
        self.center_position_y -= 1
    
    def move_downwards(self):
        self.center_position_y += 1

    def change_orientation(self):
        if self.orientation == HORIZONTAL:
            self.orientation = VERTICAL

        elif self.orientation == VERTICAL:
            self.orientation = HORIZONTAL
    
    def is_horizontal(self):
        if self.orientation == HORIZONTAL:
            return True
        else: 
            return False
    
    def is_vertical(self):
        if self.orientation == VERTICAL:
            return True
        else: 
            return False
