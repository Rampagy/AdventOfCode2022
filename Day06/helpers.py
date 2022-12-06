import parse # python -m pip install parse
import heapq

# line parsing functions
def ParseLine(search_pattern, line):
    # https://pypi.org/project/parse/
    result = parse.search(search_pattern, line)
    return list(result.fixed)


# A* functions and classes
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_surrounding_positions(self):
        return [Position(self.x + 0, self.y - 1), # North
                Position(self.x + 1, self.y + 0), # East
                Position(self.x + 0, self.y + 1), # South
                Position(self.x - 1, self.y + 0)] # West

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.x,
                                   self.y)

    def __hash__(self):
        #return ((self.x+self.y) * (self.x+self.y+1) >> 1) + self.y # cantors pairing
        return self.x * self.x + self.x + self.y if self.x >= self.y else self.x + self.y * self.y # szudziks function

def heuristic(a, b):
    return abs( (a.x - b.x) + (a.y - b.y) )

def astar_search(weighted_map, start, goal):
    # 255 is unwalkable in the weighted map
    # returns list of Position objects
    # start and goal should be Position objects
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
    fscore = {start : heuristic(start, goal)}
    oheap_copy = { start : fscore[start] }
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))


    while ( len(oheap) > 0 ):
        current = heapq.heappop(oheap)[1]
        oheap_copy.pop(current)

        if current == goal:
            # path found!
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.reverse()
            return path

        neighbors = current.get_surrounding_positions()

        for neighbor in neighbors:

            # if the neighbor is a vlid position
            if (neighbor.x >= 0 and neighbor.y >= 0 and
                    neighbor.y < mapHeight and neighbor.x < mapWidth and
                    weighted_map[neighbor.y][neighbor.x] < 255):

                neighbor_gscore = gscore[current] + weighted_map[neighbor.y][neighbor.x] + \
                                    heuristic(neighbor, current)
                neighbor_fscore = neighbor_gscore + heuristic(neighbor, goal)

                # if this neighbor is already on the open list with a smaller fscore, skip it
                open_neighbor = oheap_copy.get(neighbor)
                if (open_neighbor != None):
                    if open_neighbor <= neighbor_fscore:
                        continue
                # check if it is on the closed list
                elif neighbor in close_set:
                    if fscore.get(neighbor) <= neighbor_fscore:
                        continue
                # add to the open list
                else:
                    # track the node's parent
                    came_from[neighbor] = current

                    # gscore = cost to get from start to the curernt position
                    # hscore = estimated cost to get from the current position to the goal
                    # fscore = gscore + hscore
                    gscore[neighbor] = neighbor_gscore
                    fscore[neighbor] = neighbor_fscore

                    # add to the open list
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
                    oheap_copy[neighbor] = fscore[neighbor]

        # add current position to the already searched list
        close_set.add(current)

    return path


# djikstra functions and classes
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
            if (neighbor.x >= 0 and neighbor.y >= 0 and
                    neighbor.y < mapHeight and neighbor.x < mapWidth and
                    weighted_map[neighbor.y][neighbor.x] < 255):

                neighbor_gscore = gscore[current] + weighted_map[neighbor.y][neighbor.x] + \
                                    heuristic(neighbor, current)

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
    # ParseLine examples
    vals = ParseLine('{:d}-{:d},{:d}-{:d}', '51-88,52-87\n')
    print('ParseLine result: {}'.format(vals))

    # A* example
    map = [
        [0, 255, 0,   0, 0],
        [0, 255, 0, 255, 0],
        [0, 255, 0, 255, 0],
        [0, 255, 0, 255, 0],
        [0,   0, 0, 255, 0]
    ]
    path = astar_search(map, Position(0, 0), Position(4, 4))
    print('\nA* result: {}'.format(path))

    # Djikstra example
    path = djikstra_search(map, Position(0,0), Position(4,4))
    print('\nDjikstra result: {}'.format(path))
