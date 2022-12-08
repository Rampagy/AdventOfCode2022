import helpers

if __name__ == '__main__':
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid += [[*line.strip()]]

    max_scenic_score = 0
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            north = 0
            south = 0
            west = 0
            east = 0

            if i == 0: # top row
                north = 0
            else:
                for k in range(i-1, -1, -1):  # search north from tree
                    if grid[k][j] < tree:
                        north += 1
                    else:
                        north += 1
                        break

            if i == len(grid)-1: # bottom row
                south = 0
            else:
                for k in range(i+1, len(grid)):  # search south from tree
                    if grid[k][j] < tree:
                        south += 1
                    else:
                        south += 1
                        break

            if j == 0: # left column
                west = 0
            else:
                for k in range(j-1, -1, -1): # search west from tree
                    if grid[i][k] < tree:
                        west += 1
                    else:
                        west += 1
                        break

            if j == len(row)-1: # right column
                east = 0
            else:
                for k in range(j+1, len(row)): # search east from tree
                    if grid[i][k] < tree:
                        east += 1
                    else:
                        east += 1
                        break


            #print(i, j, ' ', tree, ' ', north,south,east,west)

            scenic_score = north*south*east*west
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

            #bigger_north_trees = [1 for k in range(i) if grid[k][j] >= tree] # north
            #bigger_south_trees = [1 for k in range(i+1, len(grid)) if grid[k][j] >= tree] # south

            #bigger_west_trees = [1 for k in range(j) if grid[i][k] >= tree] # west
            #bigger_east_trees = [1 for k in range(j+1, len(row)) if grid[i][k] >= tree] # east


            #if len(bigger_north_trees) == 0:
            #    visible_trees += 1
            #elif len(bigger_south_trees) == 0:
            #    visible_trees += 1
            #elif len(bigger_west_trees) == 0:
            #    visible_trees += 1
            #elif len(bigger_east_trees) == 0:
            #    visible_trees += 1

    print(max_scenic_score)