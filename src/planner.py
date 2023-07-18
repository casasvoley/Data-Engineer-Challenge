from labyrinth import Labyrinth

def find_minimal_number_of_moves(labyrinth: Labyrinth):

    '''
    Method that uses a breadth-first search algorithm to find the minimal
    number of moves required to carry the rod from the top left corner to
    the bottom right corner.

    The basic idea is to check all states that can be reached with 1 move,
    then all states that are reachable with 2 moves, etc. This process
    will continue until a state where the rod is in the bottom right
    corner is reached (in which case we then know the minimal number of
    moves to get there and that is output) or all possible states have
    been checked without arriving at the goal (in which case the output is
    -1).

    The states are represented as an array of 3 elements (e.g, [0, 2, 3]),
    where the numbers are respectively the orientation of the rod
    (0=horizontal, 1=vertical), the position of the center of the rod on
    the X axis and the same thing on the Y axis.

    Parameters:
        labyrinth (Labyrinth): The labyrinth whose minimal answer we wish
                               to find.
    
    Returns:
        minimal_number_of_moves (int): The minimal number of moves needed
                                       to carry the rod to the bottom right
                                       corner. If there is no possible way
                                       to get to the goal, its value is -1. 
    '''

    visited_states = []
    to_be_visited_states = []

    initial_state = [labyrinth.rod.orientation,
                     labyrinth.rod.center_position_x,
                     labyrinth.rod.center_position_y]
    visited_states.append(initial_state)
    to_be_visited_states.append(initial_state)

    


