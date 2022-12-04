if __name__ == '__main__':
    # read in text file
    count = 0
    with open('input.txt', 'r') as f:
        for line in f:
            pair = line.strip().split(',')

            chores_list = []
            for chore_ids in pair:
                end_vals = chore_ids.split('-')
                chores_list += [list(range(int(end_vals[0]), int(end_vals[1])+1))]

            issubset0 = set(chores_list[1]).issubset(set(chores_list[0]))
            issubset1 = set(chores_list[0]).issubset(set(chores_list[1]))

            if issubset1 or issubset0:
                count += 1

    print(count) # 487