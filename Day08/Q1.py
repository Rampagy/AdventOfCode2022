import helpers

if __name__ == '__main__':
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid += [[*line.strip()]]

    visible_trees = 0
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(row) or j == len(grid):
                # tree is on perimeter and is visible
                visible_trees += 1
                continue
            
            bigger_north_trees = [1 for k in range(i) if grid[k][j] >= tree] # north
            bigger_south_trees = [1 for k in range(i+1, len(grid)) if grid[k][j] >= tree] # south

            bigger_west_trees = [1 for k in range(j) if grid[i][k] >= tree] # west
            bigger_east_trees = [1 for k in range(j+1, len(row)) if grid[i][k] >= tree] # east


            if len(bigger_north_trees) == 0:
                visible_trees += 1
            elif len(bigger_south_trees) == 0:
                visible_trees += 1
            elif len(bigger_west_trees) == 0:
                visible_trees += 1
            elif len(bigger_east_trees) == 0:
                visible_trees += 1

    print(visible_trees)