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


    signal_strength = []
    for i, registerX in enumerate(regXOverTime):
        if ((i+22) % 40) == 0:
            strength = registerX*(i+2)
            signal_strength += [strength]
            print(i, registerX, strength)

    print(sum(signal_strength)) # 13060