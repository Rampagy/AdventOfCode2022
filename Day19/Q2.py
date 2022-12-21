import helpers
from collections import deque
import math
import sys

def DetermineRobotToBuild(robots, minerals, blueprint, turns):
    # determine if anything can be built
    # somehow need to determine the opportunity cost
    # every minute we have the option of choosing don't buy, or buy - > we need to traverse every option to see
    # which produces the most geodes
    max_geodes = 0
    s = (robots[0], robots[1], robots[2], robots[3], minerals[0], minerals[1], minerals[2], minerals[3], turns)
    states = deque([s])
    already_evaluated = set()
    while len(states) > 0:
            state = states.popleft()
            r0, r1, r2, r3, m0, m1, m2, m3, turns_s = state
            max_geodes = max(max_geodes, m3)

            if turns_s == 0:
                # this state has reached it's max depth - check other states
                continue

            max_ore_used_per_turn = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
            max_clay_used_per_turn = blueprint[4]
            max_obisidian_used_per_turn = blueprint[6]

            if r0 >= max_ore_used_per_turn:
                # no need to track more robots than we can use per turn
                r0 = max_ore_used_per_turn
            if r1 >= max_clay_used_per_turn:
                # no need to track more robots than we can use per turn
                r1 = max_clay_used_per_turn
            if r2 >= max_obisidian_used_per_turn:
                # no need to track more robots than we can use per turn
                r2 = max_obisidian_used_per_turn
            if m0 > turns_s*max_ore_used_per_turn - r0*(turns_s-1):
                # if we have more minerals than can possible be used for the rest of the simulation cap it
                m0 = turns_s*max_ore_used_per_turn - r0*(turns_s-1)
            if m1 > turns_s*max_clay_used_per_turn - r1*(turns_s-1):
                # if we have more minerals than can possible be used for the rest of the simulation cap it
                m1 = turns_s*max_clay_used_per_turn - r1*(turns_s-1)
            if m2 > turns_s*max_obisidian_used_per_turn - r2*(turns_s-1):
                # if we have more minerals than can possible be used for the rest of the simulation cap it
                m2 = turns_s*max_obisidian_used_per_turn - r2*(turns_s-1)


            temp_state = tuple([r0, r1, r2, r3, m0, m1, m2, m3, turns_s])
            if temp_state in already_evaluated:
                continue
            already_evaluated.add(temp_state)


            # add do nothing state
            #temp_minerals[0] += temp_robots[0]
            #temp_minerals[1] += temp_robots[1]
            #temp_minerals[2] += temp_robots[2]
            #temp_minerals[3] += temp_robots[3]

            new_state = tuple([r0, r1, r2, r3, m0+r0, m1+r1, m2+r2, m3+r3, turns_s-1])
            states.append( new_state )


            if m0 >= blueprint[5] and m2 >= blueprint[6]:
                # we can build geode robot -> add state to states to evaulate further

                #m0 += r0 - blueprint[5] # ore
                #m1 += r1 #clay
                #m2 += r2 - blueprint[6] # obsidian
                #m3 += r3 # geode
                #r3 += 1 # geode robot


                new_state = tuple([r0, r1, r2, r3+1, m0+r0 - blueprint[5], m1+r1, m2+r2-blueprint[6], m3+r3, turns_s-1])
                states.append( new_state )


            if m0 >= blueprint[3] and m1 >= blueprint[4]:
                # we can build obsidian robot -> add state to states to evaulate further
                #temp_minerals[0] += temp_robots[0] - blueprint[3] # ore
                #temp_minerals[1] += temp_robots[1] -blueprint[4] # clay
                #temp_minerals[2] += temp_robots[2] # obsidian
                #temp_minerals[3] += temp_robots[3] # geodes
                #temp_robots[2] += 1 # obsidian robot


                new_state = tuple([r0, r1, r2+1, r3, m0+r0-blueprint[3], m1+r1-blueprint[4], m2+r2, m3+r3, turns_s-1])
                states.append( new_state )


            if m0 >= blueprint[2]:
                # we can build clay robot
                #temp_minerals = minerals_s.copy() # these copy's are slowwwww....
                #temp_robots = robots_s.copy()

                #temp_minerals[0] += temp_robots[0] - blueprint[2] # ore
                #temp_minerals[1] += temp_robots[1] # clay
                #temp_minerals[2] += temp_robots[2] # obsidian
                #temp_minerals[3] += temp_robots[3] # geodes
                #temp_robots[1] += 1


                new_state = tuple([r0, r1+1, r2, r3, m0+r0-blueprint[2], m1+r1, m2+r2, m3+r3, turns_s-1])
                states.append( new_state )


            if m0 >= blueprint[1]:
                # we can build ore robot
                #temp_minerals = minerals_s.copy() # these copy's are slowwwww....
                #temp_robots = robots_s.copy()

                #temp_minerals[0] += temp_robots[0] - blueprint[1] # ore
                #temp_minerals[1] += temp_robots[1] # clay
                #temp_minerals[2] += temp_robots[2] # obsidian
                #temp_minerals[3] += temp_robots[3] # geodes
                #temp_robots[0] += 1


                new_state = tuple([r0+1, r1, r2, r3, m0+r0-blueprint[1], m1+r1, m2+r2, m3+r3, turns_s-1])
                states.append( new_state )


    return max_geodes

if __name__=='__main__':
    data = open('input.txt').read().strip()
    # (blueprint_num, ore_cost, clay_ore_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost)
    blueprints = [helpers.ParseLine('Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.', line) for line in data.split('\n')]

    max_geodes = []
    quality_scores = []
    for blueprint in blueprints[0:3]:
        minerals = [0, 0, 0, 0] # ore, clay, obsidian, geode
        robots = [1, 0, 0, 0] # ore, clay, obisdian, geode
        geodes = DetermineRobotToBuild(robots, minerals, blueprint, 32)
        max_geodes += [geodes]
        print(max_geodes)


    print(math.prod(max_geodes)) # ex=3472, input=13640