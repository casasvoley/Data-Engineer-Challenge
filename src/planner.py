from .labyrinth import Labyrinth

# Rod orientation constants
HORIZONTAL = 0
VERTICAL = 1

def find_minimal_number_of_moves(labyrinth: Labyrinth, initial_state: dict, goal: list):

    '''
    Method that uses a breadth-first search algorithm to find the minimal
    number of moves required to carry the rod from the top left corner to
    the bottom right corner.

    The basic idea is to check all new states that can be reached with 1 move,
    then all new states that are reachable with 2 moves, etc. This process
    will continue until a state where the rod is in the bottom right
    corner is reached (in which case we then know the minimal number of
    moves to get there and that is output) or all possible states have
    been checked without arriving at the goal (in which case the output is
    -1).

    The states are represented as an dicitonary of 3 elements:
        {
            "rod_orientation": 0 if horizontal, 1 if vertical
            "rod_center_position_x": the position of the center of the rod
                                     on the X axis
            "rod_center_position_y": the position of the center of the rod
                                     on the Y axis
        }

    Parameters:
        labyrinth (Labyrinth): The labyrinth whose minimal answer we wish
                               to find.
        initial_state (dict): The initial state where the rod is in.
        goal (list): The coordinates ([x,y]) of the goal cell.
    
    Returns:
        minimal_number_of_moves (int): The minimal number of moves needed
                                       to carry the rod to the bottom right
                                       corner. If there is no possible way
                                       to get to the goal, its value is -1. 
    '''

    visited_states = [] # States that have already been reached
    to_be_explored_paths = [] # Paths that can be further explored

    visited_states.append(initial_state)
    to_be_explored_paths.append([initial_state])

    while to_be_explored_paths:
        current_path = to_be_explored_paths.pop(0) # Path that we are currently expanding
        current_state = current_path[-1] # State where the current path ends

        # Check all possible moves from the current state
        neighbour_states = check_all_possible_moves(labyrinth, current_state)

        for neighbour_state in neighbour_states:
            # If the goal is reached, return the number of moves
            if is_this_state_the_goal(neighbour_state, goal):
                current_path.append(neighbour_state)
                return len(current_path)-1
            
            # If the state has been seen before, it is ignored.
            # If it is a new state, it is added to visited_states
            # and the path that ends in this state is adde to 
            # to_be_explored_paths.
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)

                new_path = current_path.copy()
                new_path.append(neighbour_state)
                to_be_explored_paths.append(new_path)

    # There is no possible path to the goal: return -1
    return -1

def check_all_possible_moves(labyrinth: Labyrinth, current_state: dict):

    '''
    Method that checks all possible moves that the rod can perform 
    from a certain state and return a list of states that can be 
    reached through those moves.

    Parameters: 
        labyrinth (Labyrinth): The labyrinth whose minimal answer
                               we wish to find.
        current_state (dict): The state that the rod is in.

    Returns:
        neighbour_states (list): A list containing all states 
                                 reachable from the current state.
    '''

    neighbour_states = []

    if labyrinth.can_the_rod_move_to_the_right(current_state):
        neighbour_state = current_state.copy()
        neighbour_state["rod_center_position_x"] += 1
        neighbour_states.append(neighbour_state)

    if labyrinth.can_the_rod_move_to_the_left(current_state):
        neighbour_state = current_state.copy()
        neighbour_state["rod_center_position_x"] -= 1
        neighbour_states.append(neighbour_state)

    if labyrinth.can_the_rod_move_upwards(current_state):
        neighbour_state = current_state.copy()
        neighbour_state["rod_center_position_y"] -= 1
        neighbour_states.append(neighbour_state)

    if labyrinth.can_the_rod_move_downwards(current_state):
        neighbour_state = current_state.copy()
        neighbour_state["rod_center_position_y"] += 1
        neighbour_states.append(neighbour_state)

    if labyrinth.can_the_rod_change_orientation(current_state):
        neighbour_state = current_state.copy()
        neighbour_state["rod_orientation"] = 1 - neighbour_state["rod_orientation"]
        neighbour_states.append(neighbour_state)
    
    return neighbour_states

def is_this_state_the_goal(state: dict, goal: list):

    '''
    Method that checks if, in a given state, the rod has reached the goal cell.

    Parameters:
        state (dict): The state where the rod is in.
        goal (list): Coordinates ([x,y]) of the cell that we wish to reach.
    
    Returns:
        A boolean stating if the rod is situated in the goal cell or not.
    '''

    if state["rod_orientation"] == HORIZONTAL:
        return goal in [[state["rod_center_position_x"]+i, 
                        state["rod_center_position_y"]] for i in range(-1,2)]

    if state["rod_orientation"] == VERTICAL: 
        return goal in [[state["rod_center_position_x"], 
                        state["rod_center_position_y"]+i] for i in range(-1,2)]
