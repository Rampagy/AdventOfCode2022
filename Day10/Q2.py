import helpers
import copy

if __name__ == '__main__':
    regXOverTime = [] # the index is the clkCount
    with open('input.txt', 'r') as f:
        regX = 1
        #regXOverTime += [regX]
        for i, line in enumerate(f):
            line = line.strip()

            if line.startswith('noop'):
                regXOverTime += [regX]
            else:
                # only other option is addx
                [op, num] = line.split()

                for j in range(1):
                    regXOverTime += [regX]

                regX += int(num)
                regXOverTime += [regX]


    i = 0
    sprite_position = regXOverTime[0]
    while  i < len(regXOverTime):
        if ((i-1)%40) == sprite_position%40 or \
                (i%40) == sprite_position%40 or \
                ((i+1)%40) == sprite_position%40:
            print('#', end ='')
        else: 
            print('.', end ='')

        if ((i+1) % 40) == 0:
            print()
        
        sprite_position = regXOverTime[i]
        i += 1

'''
I'm not sure if those one to thr right of the Z are supposed to be marked...

####...##.#..#.###..#..#.#....###..#####
#.......#.#..#.#..#.#..#.#....#..#....#.
###.....#.#..#.###..#..#.#....#..#...#.#
#.......#.#..#.#..#.#..#.#....###...#..#
#....#..#.#..#.#..#.#..#.#....#.#..#...#
#.....##...##..###...##..####.#..#.####.
'''