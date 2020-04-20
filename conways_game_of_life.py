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
    print('\n')
    current_cells = copy.deepcopy(next_cells)

    # print the current cell automata
    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end='')
        print()

    
    for x in range(width):
        for y in range(height):
            left_coordinate = (x-1) % width   # calculate coordinates of neighboring cells to current cell
            right_coordinate = (x+1) % width
            above_coordinate = (x-1) % height
            below_coordinate = (x+1) % height

            # calculate number of alive neighbors for current cell
            num_alive_neighbors = 0
            if current_cells[left_coordinate][above_coordinate] == '#': # top-left neighbor
                num_alive_neighbors += 1
            if current_cells[x][above_coordinate] == '#': # top neighbor
                num_alive_neighbors += 1
            if current_cells[right_coordinate][above_coordinate] == '#': # top-right neighbor
                num_alive_neighbors += 1
            if current_cells[left_coordinate][y] == '#': # left neighbor
                num_alive_neighbors += 1
            if current_cells[right_coordinate][y] == '#': # right neighbor
                num_alive_neighbors += 1
            if current_cells[left_coordinate][below_coordinate] == '#': # bottom-left neighbor
                num_alive_neighbors += 1
            if current_cells[x][below_coordinate] == '#': # bottom neighbor
                num_alive_neighbors += 1
            if current_cells[right_coordinate][below_coordinate] == '#': # bottom-right neighbor
                num_alive_neighbors += 1
            
            # calculate the next cell automata based on conway's game of life rules
            if current_cells[x][y] == '#' and (num_alive_neighbors == 2 or num_alive_neighbors == 3):
                # living cells with 2 or 3 alive neighbors stay alive in next generation
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_alive_neighbors == 3:
                # dead cells with 3 alive neighbors come alive in next generation
                next_cells[x][y] = '#'
            else:
                # every other cell stays dead or becomes dead
                next_cells[x][y] = ' '

    time.sleep(1) # reduce flickering

