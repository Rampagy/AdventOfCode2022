import helpers
import heapq
import math

def heuristic(a, b, allow_diagonals=False):
    if allow_diagonals:
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    else:
        return abs(a.x - b.x) + abs(a.y - b.y)


# djikstra functions and classes (with 2d map)
def djikstra_search(weighted_map, start, goal, diagonals=False):
    # 255 is unwalkable in the weighted map
    # returns list of Position objects
    # start and goal should be position objects
    # diagonals not currently allowed

    mapWidth = len(weighted_map[0])
    mapHeight = len(weighted_map)

    path = []
    if (start.x < 0) or (start.y < 0) or (goal.x >= mapWidth) or (goal.y >= mapHeight) or \
            (start == goal) or (mapWidth < 2) or (mapHeight < 2):
        return path

    close_set = set()
    came_from = dict()
    gscore = {start: 0}
    oheap_copy = { start : gscore[start] }
    oheap = []
    heapq.heappush(oheap, (gscore[start], start))

    count = 0
    while ( len(oheap) > 0 ):
        count += 1
        current = heapq.heappop(oheap)[1]
        oheap_copy.pop(current)
        close_set.add(current)

        neighbors = current.get_surrounding_positions()

        for neighbor in neighbors:

            # if the neighbor is a vlid position
            if (neighbor.x >= 0 and neighbor.y >= 0 and \
                    neighbor.y < mapHeight and neighbor.x < mapWidth and \
                    weighted_map[neighbor.y][neighbor.x] < 255) and \
                    (weighted_map[neighbor.y][neighbor.x] - weighted_map[current.y][current.x]) <= 1:

                # weighted_map[neighbor.y][neighbor.x] + \
                neighbor_gscore = gscore[current] + heuristic(neighbor, current)

                # if this neighbor is already on the open list with a smaller gscore, skip it
                open_neighbor = oheap_copy.get(neighbor)
                if (open_neighbor != None and neighbor_gscore < gscore[neighbor]):
                    # track nodes parent
                    came_from[neighbor] = current

                    # gscore = cost to get from start to the current position
                    gscore[neighbor] = neighbor_gscore

                    # update the neighbors values
                    oheap_copy[neighbor] = neighbor_gscore

                    # remove the old gscore
                    for i in range(oheap.count):
                        if oheap[i][1] == neighbor:
                            oheap.clear(i)
                            break

                    # add to the open list
                    heapq.heappush(oheap, (gscore[neighbor], neighbor))
                    continue

                # check if it is on the closed list
                if neighbor in close_set and neighbor_gscore < gscore[neighbor]:
                    # remove neighbor from closed list
                    close_set.clear(neighbor)

                # add to the open list
                if neighbor not in close_set and open_neighbor == None:
                    # track the node's parent
                    came_from[neighbor] = current

                    # gscore = cost to get from start to the current position
                    gscore[neighbor] = neighbor_gscore

                    # Add to the open list
                    oheap_copy[neighbor] = neighbor_gscore
                    heapq.heappush(oheap, (gscore[neighbor], neighbor))

    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


if __name__ == '__main__':
    grid = []
    with open('input.txt', 'r') as f:
        for i, line in enumerate(f):
            grid += [[*line.strip()]]

    START = helpers.Position(0, 0)
    END = helpers.Position(0, 0)
    search_map = []

    for i, row in enumerate(grid):
        search_map.append([])
        for j, col in enumerate(row):
            numerical_equivalent = ord(col) - 97
            if col == 'S':
                START.x = j
                START.y = i
                numerical_equivalent = 0
            elif col == 'E':
                END.x = j
                END.y = i
                numerical_equivalent = 25

            search_map[i].append(numerical_equivalent)

    path = djikstra_search(search_map, START, END)

    # print map
    for p in path:
        grid[p.y][p.x] = '*'

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            print(col, end = '')
        print()

    print(len(path)) # 520