from src.labyrinth import Labyrinth
from src.planner import find_minimal_number_of_moves

layout = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
          ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
          ['.', '#', '.', '.', '.', '.', '.', '#', '.']]

initial_state = {
    "rod_orientation": 0,
    "rod_center_position_x": 1,
    "rod_center_position_y": 0
    }

goal = [len(layout[0])-1, len(layout)-1]

labyrinth = Labyrinth(layout)

number_of_moves = find_minimal_number_of_moves(labyrinth=labyrinth, initial_state=initial_state, goal=goal)

print(f"It takes {number_of_moves} moves to carry the rod to the goal.")