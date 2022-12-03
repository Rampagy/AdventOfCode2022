if __name__ == '__main__':
    # read in text file
    with open('input.txt', 'r') as f:
        total = 0
        for line in f:
            compartment_size = int(len(line.strip()) / 2)

            for i in range(compartment_size):
                if line.strip()[i] in line.strip()[compartment_size:]:
                    score = 0
                    if ord(line.strip()[i]) >= ord('A') and \
                            ord(line.strip()[i]) <= ord('Z'):
                        # uppercase
                        score= ord(line.strip()[i]) - 38
                    else:
                        # lowercase
                        score= ord(line.strip()[i]) - ord('a') + 1
                    
                    total += score

                    break

    print(total) # 7889