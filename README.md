<h1>Data Engineer Challenge</h1>

## About

Challenge made to evaluate coding abilities.

## Challenge

The goal is to carry the rod from the top left corner of the labyrinth to the bottom right corner. This rod is not exactly the lightest thing you can imagine, so the participant would naturally want to do it as fast as possible.

Find the minimal number of moves required to carry the rod through the labyrinth. The labyrinth can be represented as a rectangular matrix, some cells of which are marked as blocked, and the rod can be represented as a 1 × 3 rectangle. The rod can't collide with the blocked cells or the walls, so it's impossible to move it into a position in which one of its cells coincides with the blocked cell or the wall. The goal is thus to move the rod into position in which one of its cells is in the bottom right cell of the labyrinth.

**Input**

- labyrinth : List [List [ str ] ]

    A rectangular array of chars representing the labyrinth, where labyrinth[i][j] = '.' if the corresponding cell is empty and labyrinth[i][j] = '#' if the corresponding cell is blocked.

    Guaranteed constraints:

    &emsp;&emsp;3 ≤ labyrinth.length ≤ 1000,   
    &emsp;&emsp;3 ≤ labyrinth[i].length ≤ 1000

**Output**

- result : Integer

    A number of moves required to carry the rod to the end of labyrinth or -1 if it is impossible.

## Solution approach

To solve this problem, a breadth-first algorythm has been used, which is implemented in the method <code>find_minimal_number_of_moves</code> of the module <code>planner.py</code>.

The algorythm starts from the initial position and orientation of the rod (which we will call a state from now on). Then checks what moves the rod can perform. If one of the states that are reachable through those moves is the goal, we have finished. If not, the algorythm checks which of the reachable states have never been seen before and stores these new path that are yet to be explored in a queue. Finally, we take the first unexplored path from the queue and repeat the process until we find a path that gets to the goal.

If at some point the queue becomes empty, that means that all possible states have been explored and therefore it is impossible to carry the rod to the goal.

This algorythm checks all new states that are reachable with 1 move, then all new states that are possible with 2 moves, etc. That means that if the goal is reached, it will be reached with the minimal number of moves.

## Running

The script <code>main.py</code> can be used to play around defining any labyrinth layout, initial state and goal. It will print out the minimal number of moves to carry the rod to the goal.

## Tests

The [pytest](https://docs.pytest.org/en/stable/) framework is recommended to perform the tests.

Install pytest:

```sh
pip install pytest
```

Run the tests:

```sh
pytest
```

**When you contribute, you need to add tests on the features you add.**

## Built Using

- [Python](https://www.python.org/) - Language
- [pytest](https://docs.pytest.org/en/stable/) - Testing framework

