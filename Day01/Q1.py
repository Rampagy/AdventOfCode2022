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

    max_cals = 0
    for elf in numbers:
        elf_cals = sum(elf)

        if elf_cals > max_cals:
            max_cals = elf_cals

    print(max_cals) # 67658