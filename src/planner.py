from labyrinth import Labyrinth

def find_minimal_number_of_moves(labyrinth: Labyrinth, initial_state: dict):

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
    
    Returns:
        minimal_number_of_moves (int): The minimal number of moves needed
                                       to carry the rod to the bottom right
                                       corner. If there is no possible way
                                       to get to the goal, its value is -1. 
    '''

    visited_states = []
    to_be_visited_states = []

    visited_states.append(initial_state)
    to_be_visited_states.append(initial_state)

    while to_be_visited_states:
        current_state = to_be_visited_states.pop(0)

        # Check all possible moves from the current state

        if labyrinth.can_the_rod_move_to_the_right(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_x"] += 1

            # If the state has been seen before, it is not added
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                to_be_visited_states.append(neighbour_state)

        if labyrinth.can_the_rod_move_to_the_left(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_x"] -= 1

            # If the state has been seen before, it is not added
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                to_be_visited_states.append(neighbour_state)

        if labyrinth.can_the_rod_move_upwards(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_y"] -= 1

            # If the state has been seen before, it is not added
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                to_be_visited_states.append(neighbour_state)

        if labyrinth.can_the_rod_move_downwards(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_center_position_y"] += 1

            # If the state has been seen before, it is not added
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                to_be_visited_states.append(neighbour_state)

        if labyrinth.can_the_rod_change_orientation(current_state):
            neighbour_state = current_state.copy()
            neighbour_state["rod_orientation"] = 1 - neighbour_state["rod_orientation"]

            # If the state has been seen before, it is not added
            if not neighbour_state in visited_states:
                visited_states.append(neighbour_state)
                to_be_visited_states.append(neighbour_state)


    labyrinth

layout = [['.', '.', '.', '.'],
          ['.', '.', '.', '.'],
          ['.', '.', '.', '.']]
initial_state = {"rod_orientation": 0,
                 "rod_center_position_x": 1,
                 "rod_center_position_y": 0}
print(initial_state.items())
l = Labyrinth(layout)
find_minimal_number_of_moves(l,initial_state)


