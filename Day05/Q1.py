import helpers

if __name__ == '__main__':
    # read in text file
    before_moves = True
    list_box_stack = []
    dict_box_stack = {}
    moves = []

    with open('input.txt', 'r') as f:
        for line in f:
            if line.strip() == '':
                before_moves = False
            elif before_moves:
                boxes = [line[i:i+4] for i in range(0, len(line), 4)]
                box_row = []
                for i, box in enumerate(boxes):
                    if box.strip() != '':
                        box_row += [box.strip()]
                    else:
                        box_row += ['']
                list_box_stack += [box_row]
            else:
                move = helpers.ParseLine('move {:d} from {:d} to {:d}', line)
                moves += [move]

        # remove box stack labels
        stacks = list_box_stack.pop(len(list_box_stack)-1)

        # initialize dict with lists
        for i, stack in enumerate(stacks):
            dict_box_stack[i+1] = []

        # convert from list to dict
        for row_num, row in enumerate(list_box_stack):
            for i, box in enumerate(row):
                if box != '':
                    box = box.strip('[').strip(']')
                    dict_box_stack[i+1] += [box]

        for k, _ in dict_box_stack.copy().items():
            dict_box_stack[k].reverse()

        for boxes_to_move, stack_start, stack_end in moves:
            for i in range(boxes_to_move):
                dict_box_stack[stack_end] += [dict_box_stack[stack_start].pop()]
        
        solution = ''
        for _, v in dict_box_stack.items():
            solution += v[-1]

        print(solution) # ZRLJGSCTR
