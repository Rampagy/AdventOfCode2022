import helpers

ROW_NUM = 2000000

if __name__=='__main__':
    data = open('input.txt').read().strip()
    points = [helpers.ParseLine('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}!', line+'!') for line in data.split('\n')]

    non_beacon_points = set()
    beacons = set()
    potential_x = set([helpers.Position(x, ROW_NUM) for x in range(-1000000, 5500000)])
    for point in points:
        print(point)
        sensor = helpers.Position(point[0], point[1])
        beacon = helpers.Position(point[2], point[3])

        if beacon not in beacons:
            beacons.add(beacon)

        for search_pos in potential_x.copy():
            #search_pos = helpers.Position(x, ROW_NUM)
            if helpers.heuristic(sensor, beacon) >= helpers.heuristic(sensor, search_pos) and \
                    search_pos not in non_beacon_points and search_pos is not beacon:
                non_beacon_points.add(search_pos)
                potential_x.remove(search_pos)

    # remove any beacons from the non beacon list
    for b in beacons:
        if b in non_beacon_points:
            non_beacon_points.remove(b)

    print(len(non_beacon_points)) # 5100463