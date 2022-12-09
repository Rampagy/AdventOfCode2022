import helpers
import copy

if __name__ == '__main__':
    head = helpers.Position(0,0)
    tail = helpers.Position(0,0)
    all_tail_locations = [tail]

    with open('input.txt', 'r') as f:
        for line in f:
            [direction, distance] = helpers.ParseLine('{} {:d}', line)
            for _ in range(distance):

                prev_head = copy.copy(head)
                if direction == 'U':
                    # up
                    head.y -= 1
                elif direction == 'D':
                    # down
                    head.y += 1
                elif direction == 'L':
                    # left
                    head.x -= 1
                elif direction == 'R':
                    head.x += 1
                else:
                    # do nothing?
                    pass
                
                separation = helpers.heuristic(head, tail, allow_diagonals=True)
                if separation > 1.5:
                    # if the head and tail are greater than 1.5 away from each other
                    # update the tails position to the previous head position
                    # diagonals will be 1.414 apart
                    tail = prev_head
                    all_tail_locations += [tail]

    print(len(set(all_tail_locations)))