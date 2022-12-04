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

            # original solution
            #for chore in chores_list[0]:
            #    if chore in chores_list[1]:
            #        count += 1
            #        break

            # improved solution
            intersection_vals = set(chores_list[0]).intersection(set(chores_list[1]))
            if len(intersection_vals) > 0:
                count += 1

    print(count) # 849