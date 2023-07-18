from .labyrinth import Labyrinth

# Rod orientation constants
HORIZONTAL = 0
VERTICAL = 1

def find_minimal_number_of_moves(labyrinth: Labyrinth, initial_state: dict, goal: list):

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
    to_be_expanded_paths = [] # Paths that can be further expanded

    visited_states.append(initial_state)
    to_be_expanded_paths.append([initial_state])

    while to_be_expanded_paths:
        current_path = to_be_expanded_paths.pop(0) # Path that we are currently expanding
        current_state = current_path[-1] # State where the current path ends

        # Check all possible moves from the current state

        if labyrinth.can_the_rod_move_to_the_right(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_x"] += 1

            if is_current_state_the_goal(neighbour_state, goal):
                current_path.append(neighbour_state)
                return len(current_path)-1

            # If the state has been seen before, it is disregarded
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                new_path = current_path.copy()
                new_path.append(neighbour_state)
                to_be_expanded_paths.append(new_path)

        if labyrinth.can_the_rod_move_to_the_left(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_x"] -= 1

            if is_current_state_the_goal(neighbour_state, goal):
                current_path.append(neighbour_state)
                return len(current_path)-1

            # If the state has been seen before, it is disregarded
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                new_path = current_path.copy()
                new_path.append(neighbour_state)
                to_be_expanded_paths.append(new_path)

        if labyrinth.can_the_rod_move_upwards(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_y"] -= 1

            if is_current_state_the_goal(neighbour_state, goal):
                current_path.append(neighbour_state)
                return len(current_path)-1

            # If the state has been seen before, it is disregarded
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                new_path = current_path.copy()
                new_path.append(neighbour_state)
                to_be_expanded_paths.append(new_path)

        if labyrinth.can_the_rod_move_downwards(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_y"] += 1

            if is_current_state_the_goal(neighbour_state, goal):
                current_path.append(neighbour_state)
                return len(current_path)-1

            # If the state has been seen before, it is disregarded
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                new_path = current_path.copy()
                new_path.append(neighbour_state)
                to_be_expanded_paths.append(new_path)

        if labyrinth.can_the_rod_change_orientation(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_orientation"] = 1 - neighbour_state["rod_orientation"]

            if is_current_state_the_goal(neighbour_state, goal):
                current_path.append(neighbour_state)
                return len(current_path)-1

            # If the state has been seen before, it is disregarded
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                new_path = current_path.copy()
                new_path.append(neighbour_state)
                to_be_expanded_paths.append(new_path)

    return -1

def is_current_state_the_goal(current_state: dict, goal: list):

    '''
    Method that checks if, in a given state, the rod has reached the goal cell.

    Parameters:
        current_state (dict): The state where the rod is in.
        goal (list): Coordinates ([x,y]) of the cell that we wish to reach.
    
    Returns:
        A boolean stating if the rod is situated in the goal cell or not.
    '''

    if current_state["rod_orientation"] == HORIZONTAL:
        return goal in [[current_state["rod_center_position_x"]+i, 
                        current_state["rod_center_position_y"]] for i in range(-1,2)]

    if current_state["rod_orientation"] == VERTICAL: 
        return goal in [[current_state["rod_center_position_x"], 
                        current_state["rod_center_position_y"]+i] for i in range(-1,2)]
