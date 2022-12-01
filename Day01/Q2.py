if __name__ == '__main__':
    # read in text file
    numbers = []
    with open('input.txt', 'r') as f:
        elf_list = []
        for line in f:
            if line.strip() != '':
                elf_list += [int(line.strip())]
            else:
                numbers += [elf_list]
                elf_list = []

    max_cals = [0]*3
    for elf in numbers:
        elf_cals = sum(elf)

        # improved method that solved the puzzle
        for i in range(len(max_cals)):
            if elf_cals > max_cals[i]:
                # loop through from enf of list to i shifting all the values down one index
                # so the list remains sorted
                for j in range(len(max_cals)-1, i-1, -1):
                    max_cals[j] = max_cals[j-1]
                
                # overwrite the one it's bigger than
                max_cals[i] = elf_cals
                break

        # orignal method that solved the puzzle
        #if elf_cals > max_cals[0]:
        #    max_cals[2] = max_cals[1]
        #    max_cals[1] = max_cals[0]
        #    max_cals[0] = elf_cals
        #elif elf_cals > max_cals[1]:
        #    max_cals[2] = max_cals[1]
        #    max_cals[1] = elf_cals
        #elif elf_cals > max_cals[2]:
        #    max_cals[2] = elf_cals

    print(sum(max_cals), max_cals) # 200158