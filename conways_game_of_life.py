# The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970
# It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.
# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
#     1. Any live cell with two or three live neighbors survives.
#     2. Any dead cell with three live neighbors becomes a live cell.
#     3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
# The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

print('*' * 99)
print("The Game of Life\n\n")

import random, copy, time

next_cells = []
width = 30
height = 10

# create container grid for game and add initial cell automata
for w in range(width):
    column = []
    for h in range(height):
        if random.randint(0,1) == 1:
            column.append('#') # cell is alive
        else:
            column.append(' ') # cell is dead
    next_cells.append(column) # next_cells will be a list of list of columns


while True:  # main program loop
    print('\n' * 5)
    current_cells = copy.deepcopy(next_cells)

    # print the current cells
    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end='')
        print()
    time.sleep(1)

