print('*' * 99)
print("The Game of Life by John Horton Conway (1970)\n\n")

import random, copy, time

next_cells = []
width = 60
height = 20

# create container grid for game and add initial cell automata
for w in range(width):
    column = []
    for h in range(height):
        column.append(random.choice([' ', '#']))
    next_cells.append(column)


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

