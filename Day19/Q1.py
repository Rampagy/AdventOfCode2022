import helpers
from collections import deque

def DetermineRobotToBuild(robots, minerals, blueprint, turns):
    # determine if anything can be built
    # somehow need to determine the opportunity cost
    # every minute we have the option of choosing don't buy, or buy - > we need to traverse every option to see
    # which produces the most geodes
    max_geodes = 0
    s = (robots, minerals, turns)
    states = deque([s])
    already_evaluated = set()
    while len(states) > 0:
            state = states.popleft()
            robots_s, minerals_s, turns_s = state
            max_geodes = max(max_geodes, minerals_s[3])

            temp_state = tuple(robots_s + minerals_s + [turns_s])
            if turns_s == 0 or temp_state in already_evaluated:
                # this state has reached it's max depth - check other states OR
                # this state has already been reached - no need to re-evaluate
                continue
            already_evaluated.add(temp_state)

            # possible optimizations:
            # no need to have more ore than you can use per turn...
            # no need to have more ore robots that ore you can use per turn... 
            # so if I can these two values then it should reduce the states that need to be saved as 
            # they would produce the same result just with different turns
            max_ore_used_per_turn = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
            max_clay_used_per_turn = blueprint[3]
            max_obisidian_used_per_turn = blueprint[6]

            # add do nothing state
            temp_minerals = minerals_s.copy()
            temp_robots = robots_s.copy()

            temp_minerals[0] += temp_robots[0]
            temp_minerals[1] += temp_robots[1]
            temp_minerals[2] += temp_robots[2]
            temp_minerals[3] += temp_robots[3]

            new_state = (temp_robots, temp_minerals, turns_s-1)
            if tuple(new_state[0] + new_state[1] + [new_state[2]]) not in already_evaluated:
                states.append( new_state )


            if minerals_s[0] >= blueprint[5] and minerals_s[2] >= blueprint[6]:
                # we can build geode robot -> add state to states to evaulate further
                temp_minerals = minerals_s.copy()
                temp_robots = robots_s.copy()

                temp_minerals[0] += temp_robots[0] - blueprint[5] # ore
                temp_minerals[1] += temp_robots[1] #clay
                temp_minerals[2] += temp_robots[2] - blueprint[6] # obsidian
                temp_minerals[3] += temp_robots[3] # geode
                temp_robots[3] += 1 # geode robot


                new_state = (temp_robots, temp_minerals, turns_s-1)
                if tuple(new_state[0] + new_state[1] + [new_state[2]]) not in already_evaluated:
                    states.append( new_state )


            if minerals_s[0] >= blueprint[3] and minerals_s[1] >= blueprint[4] and robots_s[2] < max_obisidian_used_per_turn:
                # we can build obsidian robot -> add state to states to evaulate further
                # optimization: why build another obsidian robot if we already have enough obsidian robots to satisfy the max obsidian we can use per turn..
                temp_minerals = minerals_s.copy()
                temp_robots = robots_s.copy()

                temp_minerals[0] += temp_robots[0] - blueprint[3] # ore
                temp_minerals[1] += temp_robots[1] -blueprint[4] # clay
                temp_minerals[2] += temp_robots[2] # obsidian
                temp_minerals[3] += temp_robots[3] # geodes
                temp_robots[2] += 1 # obsidian robot


                new_state = (temp_robots, temp_minerals, turns_s-1)
                if tuple(new_state[0] + new_state[1] + [new_state[2]]) not in already_evaluated:
                    states.append( new_state )


            if minerals_s[0] >= blueprint[2] and robots[1] < max_clay_used_per_turn:
                # we can build clay robot
                # optimization: why build another clay robot if we already have enough clay robots to satisfy the max clay we can use per turn..
                temp_minerals = minerals_s.copy()
                temp_robots = robots_s.copy()

                temp_minerals[0] += temp_robots[0] - blueprint[2] # ore
                temp_minerals[1] += temp_robots[1] # clay
                temp_minerals[2] += temp_robots[2] # obsidian
                temp_minerals[3] += temp_robots[3] # geodes
                temp_robots[1] += 1


                new_state = (temp_robots, temp_minerals, turns_s-1)
                if tuple(new_state[0] + new_state[1] + [new_state[2]]) not in already_evaluated:
                    states.append( new_state )


            if minerals_s[0] >= blueprint[1] and robots_s[0] < max_ore_used_per_turn:
                # we can build ore robot
                # optimization: why build another ore robot if we already have enough ore robots to satisfy the max ore we can use per turn..
                temp_minerals = minerals_s.copy()
                temp_robots = robots_s.copy()

                temp_minerals[0] += temp_robots[0] - blueprint[1] # ore
                temp_minerals[1] += temp_robots[1] # clay
                temp_minerals[2] += temp_robots[2] # obsidian
                temp_minerals[3] += temp_robots[3] # geodes
                temp_robots[0] += 1


                new_state = (temp_robots, temp_minerals, turns_s-1)
                if tuple(new_state[0] + new_state[1] + [new_state[2]]) not in already_evaluated:
                    states.append( new_state )


    return max_geodes

if __name__=='__main__':
    data = open('input.txt').read().strip()
    # (blueprint_num, ore_cost, clay_ore_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost)
    blueprints = [helpers.ParseLine('Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.', line) for line in data.split('\n')]

    max_geodes = []
    quality_scores = []
    for blueprint in blueprints:
        minerals = [0, 0, 0, 0] # ore, clay, obsidian, geode
        robots = [1, 0, 0, 0] # ore, clay, obisdian, geode
        geodes = DetermineRobotToBuild(robots, minerals, blueprint, 24)
        quality_scores += [blueprint[0]*geodes]
        max_geodes += [geodes]
        print(quality_scores, max_geodes)


    print(sum(quality_scores)) # 1294