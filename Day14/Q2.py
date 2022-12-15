import helpers

if __name__=='__main__':
    data = open('input.txt').read().strip()

    sand_start = helpers.Position(500,0)
    rock_map = set()
    max_map_bounds = helpers.Position(-9999999, -999999999)
    min_map_bounds = helpers.Position( 9999999,  0) # y has to be zero here because that's where the sand drops from

    for rocks in data.split('\n'):
        rock_positions = rocks.split(' -> ')
        for i in range(1, len(rock_positions)):
            # add a straight line between the two points
            [x, y] = rock_positions[i].split(',')
            [p_x, p_y] = rock_positions[i-1].split(',')

            x = int(x)
            y = int(y)
            p_x = int(p_x)
            p_y = int(p_y)

            # update min map bounds
            if x < min_map_bounds.x:
                min_map_bounds.x = x
            if p_x < min_map_bounds.x:
                min_map_bounds.x = p_x
            if y < min_map_bounds.y:
                min_map_bounds.y = y
            if p_y < min_map_bounds.y:
                min_map_bounds.y = p_y

            # update max map bounds
            if x > max_map_bounds.x:
                max_map_bounds.x = x
            if p_x > max_map_bounds.x:
                max_map_bounds.x = p_x
            if y > max_map_bounds.y:
                max_map_bounds.y = y
            if p_y > max_map_bounds.y:
                max_map_bounds.y = p_y

            new_r = helpers.Position(x, y)
            prev_r = helpers.Position(p_x, p_y)

            delta = new_r - prev_r
            
            stepx = 0
            if delta.x < 0:
                stepx = -1
            elif delta.x > 0:
                stepx = 1

            stepy = 0
            if delta.y < 0:
                stepy = -1
            elif delta.y > 0:
                stepy = 1

            # add all x translation positions to the rock map
            if stepx != 0:
                for j in range(prev_r.x, new_r.x + stepx, stepx):
                    temp_r = helpers.Position(j, prev_r.y)
                    if temp_r not in rock_map:
                        rock_map.add(temp_r)

            # add all y translation positions to the rock map
            if stepy != 0:
                for j in range(prev_r.y, new_r.y + stepy, stepy):
                    temp_r = helpers.Position(prev_r.x, j)
                    if temp_r not in rock_map:
                        rock_map.add(temp_r)


    sand_bags = set()
    sand_bag_valid = True
    max_map_bounds.y += 2
    while sand_start not in sand_bags:
        sand_bag = sand_start.copy()

        while sand_start not in sand_bags:

            down_pos = sand_bag + helpers.Position(0, 1)
            diag_left_pos = sand_bag + helpers.Position(-1, 1)
            diag_right_pos = sand_bag + helpers.Position(1, 1)

            if down_pos not in rock_map and down_pos not in sand_bags and down_pos.y < max_map_bounds.y:
                sand_bag = down_pos
            elif diag_left_pos not in rock_map and diag_left_pos not in sand_bags and down_pos.y < max_map_bounds.y:
                sand_bag = diag_left_pos
            elif diag_right_pos not in rock_map and diag_right_pos not in sand_bags and down_pos.y < max_map_bounds.y:
                sand_bag = diag_right_pos
            else:
                # no valid positions to go to and not off the map
                # add to settled sand_bags and start dropping another one
                sand_bags.add(sand_bag)
                break

    print(len(sand_bags)) # 26484
