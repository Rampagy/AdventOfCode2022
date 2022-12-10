import helpers
import copy

NUMBER_KNOTS = 10

if __name__ == '__main__':
    knots = []
    for i in range(NUMBER_KNOTS):
        knots.append(helpers.Position(0,0))

    all_tail_locations = [knots[-1]]

    with open('input.txt', 'r') as f:
        for i, line in enumerate(f):
            [direction, distance] = helpers.ParseLine('{} {:d}\n', line)

            prev_knots = []
            for pos in knots:
                prev_knots += [copy.deepcopy(pos)]

            for _ in range(distance):
                delta = helpers.Position(0,0)
                if direction == 'U':
                    # up
                    knots[0].y -= 1
                    delta.y -= 1
                elif direction == 'D':
                    # down
                    knots[0].y += 1
                    delta.y += 1
                elif direction == 'L':
                    # left
                    knots[0].x -= 1
                    delta.x -= 1
                elif direction == 'R':
                    knots[0].x += 1
                    delta.x += 1
                else:
                    # do nothing?
                    pass


                for j in range(1, NUMBER_KNOTS):
                    #separation = helpers.heuristic(knots[j], knots[j-1], allow_diagonals=True)
                    deltax = abs(knots[j].x - knots[j-1].x) # 1
                    deltay =  abs(knots[j].y - knots[j-1].y) # 2
                    if (deltax == 2 and deltay == 0) or (deltay == 2 and deltax == 0):

                        tempdeltax = knots[j-1].x - knots[j].x
                        if tempdeltax > 1:
                            tempdeltax = 1
                        elif tempdeltax < -1:
                            tempdeltax = -1

                        tempdeltay = knots[j-1].y - knots[j].y
                        if tempdeltay > 1:
                            tempdeltay = 1
                        elif tempdeltay < -1:
                            tempdeltay = -1

                        #knots[j] = helpers.Position(knots[j].x + delta.x, knots[j].y + delta.y)
                        knots[j] = helpers.Position(knots[j].x + tempdeltax, knots[j].y + tempdeltay)

                    elif (deltax == 2 and deltay == 1) or (deltax == 1 and deltay == 2): # and (knots[j].x != knots[j-1].x or knots[j].y != knots[j-1].y):
                        # if the head and tail are greater than 1.5 away from each other
                        # update the tails position to the previous head position
                        # diagonals will be 1.414 apart
                        tempdeltax = knots[j-1].x - knots[j].x
                        if tempdeltax > 1:
                            tempdeltax = 1
                        elif tempdeltax < -1:
                            tempdeltax = -1

                        tempdeltay = knots[j-1].y - knots[j].y
                        if tempdeltay > 1:
                            tempdeltay = 1
                        elif tempdeltay < -1:
                            tempdeltay = -1

                        knots[j] = helpers.Position(knots[j].x + tempdeltax, knots[j].y + tempdeltay)

                    elif deltax > 1 and deltay > 1:
                        tempdeltax = knots[j-1].x - knots[j].x
                        if tempdeltax > 1:
                            tempdeltax = 1
                        elif tempdeltax < -1:
                            tempdeltax = -1

                        tempdeltay = knots[j-1].y - knots[j].y
                        if tempdeltay > 1:
                            tempdeltay = 1
                        elif tempdeltay < -1:
                            tempdeltay = -1

                        knots[j] = helpers.Position(knots[j].x + tempdeltax, knots[j].y + tempdeltay)


                all_tail_locations += [copy.deepcopy(knots[-1])]
            #print(direction, distance, knots)

    print(len(set(all_tail_locations)))