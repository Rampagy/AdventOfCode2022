import helpers

ROW_NUM = 4000000
MAX_X_Y = 4000000

if __name__=='__main__':
    data = open('input.txt').read().strip()
    points = [helpers.ParseLine('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}!', line+'!') for line in data.split('\n')]

    potential_x = set()

    s_and_b = set([(helpers.Position(point[0], point[1]), helpers.Position(point[2], point[3])) for point in points])
    beacons = set( [ helpers.Position(point[2], point[3]) for point in points ] )
    sensors = set( [ helpers.Position(point[0], point[1]) for point in points ] )
    s_and_b_len = len(s_and_b)

    # if there is only one beacon, then item must be d+1 away from one of the sensors
    for [sensor, beacon] in s_and_b:
        print(sensor, beacon)
        d = helpers.heuristic(sensor, beacon)
        d += 1

        for dx in range(d):
            dy = d - dx

            for signx in [-1, 1]:
                for signy in [-1, 1]:
                    search_pos = helpers.Position(sensor.x + signx*dx, sensor.y + signy*dy)

                    if search_pos.x >=0 and search_pos.x <= MAX_X_Y and \
                            search_pos.y >= 0 and search_pos.y <= MAX_X_Y and \
                            search_pos not in beacons and search_pos not in sensors:
                        if search_pos not in potential_x:
                            potential_x.add(search_pos)


    for potential in potential_x:
        count = 0
        for [sensor, beacon] in s_and_b:
            if helpers.heuristic(sensor, beacon) < helpers.heuristic(potential, sensor):
                count += 1

        if count >= s_and_b_len:
            print(potential, potential.x * 4000000 + potential.y) # 11557863040754
