if __name__ == '__main__':
    # read in text file
    with open('input.txt', 'r') as f:
        total = 0
        file = []
        for line in f:
            file += [line.strip()]

            if len(file) % 3 == 0 and len(file) > 0:
                elfs = file[-3:]
                print(elfs, file[-3:], file)

                # find intersection
                common = set.intersection(*map(set, elfs))
                letter = common.pop()

                if ord(letter) >= ord('A') and \
                        ord(letter) <= ord('Z'):
                    # uppercase
                    score= ord(letter) - 38
                else:
                    # lowercase
                    score= ord(letter) - ord('a') + 1
                total += score

    print(total) # 2825